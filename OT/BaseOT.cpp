#include "OT/BaseOT.h"
#include "Tools/random.h"
#include "Tools/benchmarking.h"
#include "Tools/Bundle.h"

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <pthread.h>

extern "C"
{
#ifndef NO_AVX_OT
#include "SimpleOT/ot_sender.h"
#include "SimpleOT/ot_receiver.h"
#endif
#include "SimplestOT_C/ref10/ot_sender.h"
#include "SimplestOT_C/ref10/ot_receiver.h"
}

// #define TEE_OT_DEBUG
// #define TEE_RANDOM_OT
// #define NORMAL_OT
// #define DEBUG_OUTPUT

using namespace std;

const char *role_to_str(OT_ROLE role)
{
    if (role == RECEIVER)
        return "RECEIVER";
    if (role == SENDER)
        return "SENDER";
    return "BOTH";
}

OT_ROLE INV_ROLE(OT_ROLE role)
{
    if (role == RECEIVER)
        return SENDER;
    if (role == SENDER)
        return RECEIVER;
    else
        return BOTH;
}

void print_octet_stream_hex(const octet *data, size_t size)
{
    std::cerr << "length - " << std::dec << size << std::endl;
    for (size_t i = 0; i < size; ++i)
    {
        std::cerr << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(data[i]) << " ";
    }
    std::cerr << std::endl;
}

void send_if_ot_sender(TwoPartyPlayer *P, vector<octetStream> &os, OT_ROLE role)
{
    if (role == SENDER)
    {
        P->send(os[0]);
    }
    else if (role == RECEIVER)
    {
        P->receive(os[1]);
    }
    else
    {
        // both sender + receiver
        P->send_receive_player(os);
    }
}

void send_if_ot_receiver(TwoPartyPlayer *P, vector<octetStream> &os, OT_ROLE role)
{
    // std::cerr << "INVOKE THIS IN THIS OT RECEIVER FUNCTION" << std::endl;
    if (role == RECEIVER)
    {
        P->send(os[0]);
    }
    else if (role == SENDER)
    {
        P->receive(os[1]);
    }
    else
    {
        // both
        P->send_receive_player(os);
    }
}

// type-dependent redirection

void sender_genS(ref10_SENDER *s, unsigned char *S_pack)
{
    ref10_sender_genS(s, S_pack);
}

void sender_keygen(ref10_SENDER *s, unsigned char *Rs_pack,
                   unsigned char (*keys)[4][HASHBYTES])
{
    ref10_sender_keygen(s, Rs_pack, keys);
}

void receiver_maketable(ref10_RECEIVER *r)
{
    ref10_receiver_maketable(r);
}

void receiver_procS(ref10_RECEIVER *r)
{
    ref10_receiver_procS(r);
}

void receiver_rsgen(ref10_RECEIVER *r, unsigned char *Rs_pack,
                    unsigned char *cs)
{
    ref10_receiver_rsgen(r, Rs_pack, cs);
}

void receiver_keygen(ref10_RECEIVER *r, unsigned char (*keys)[HASHBYTES])
{
    ref10_receiver_keygen(r, keys);
}

void BaseOT::exec_base(bool new_receiver_inputs)
{
#ifdef TEE_RANDOM_OT
    exec_base_tee_rot<SIMPLEOT_SENDER, SIMPLEOT_RECEIVER>(new_receiver_inputs);
#endif
#ifdef TEE_OT_DEBUG
    exec_base_tee<SIMPLEOT_SENDER, SIMPLEOT_RECEIVER>(new_receiver_inputs);
#endif
#ifdef NORMAL_OT
#ifndef NO_AVX_OT
    if (cpu_has_avx(true))
        exec_base<SIMPLEOT_SENDER, SIMPLEOT_RECEIVER>(new_receiver_inputs);
    else
#endif
        exec_base<ref10_SENDER, ref10_RECEIVER>(new_receiver_inputs);
#endif
}


template <class T, class U>
void BaseOT::exec_base_tee_rot(bool new_receiver_inputs){

    size_t len;
    vector<octetStream> os(2);
    PRNG G;

    T sender;
    U receiver;

    size_t unit_length = sender_inputs[0][0].size_bytes(); // 16 bytes

    os[0].reset_write_head();
    os[1].reset_write_head();

    // 1 - 1 sender set a random seed and send to the receiver.
    // set the random seed.
    octet *seed = new octet[16];
    for(int i=0; i<16; i++) seed[i] = G.get_uchar();
    os[0].store_bytes(seed, 16);

    // send the seed to the receiver.
    P->send_receive_player(os);

    // 1 - 2 receiver generates the choice bits is new_receiver_inputs is true.
    if(new_receiver_inputs){
        for(int i=0; i<nOT; i++){
            // receiver_inputs.set_bit(i, 1);
            receiver_inputs.set_bit(i, G.get_uchar() & 1);
        }
    }


    // 2 - sender: generate the two inputs.
    G.SetSeed(seed);

#ifdef DEBUG_OUTPUT
     std::cerr << "seed sender" << std::endl;
     print_octet_stream_hex(seed, 16);
    // for(int i=0; i<16; i++){
    //     std::cerr << seed[i] << std::endl;
    // }
#endif

    for(int i=0; i<nOT; i++){
        for(size_t j=0; j<unit_length; j++) {
            for(size_t k = 0; k < 8; k++){
                bool tmp_bit = G.get_uchar() & 1;
                sender_inputs[i][0].set_bit(j*8+k, tmp_bit ^ 0);
                sender_inputs[i][1].set_bit(j*8+k, tmp_bit ^ 1);
            }
        }
    }

#ifdef DEBUG_OUTPUT
    std::cerr << "sender inputs 0 - " << std::endl;
    for(int i=0; i<nOT; i++){
        print_octet_stream_hex(sender_inputs[i][0].get_ptr(), unit_length);   
    }

    std::cerr << "sender inputs 1 - " << std::endl;
    for(int i=0; i<nOT; i++) print_octet_stream_hex(sender_inputs[i][1].get_ptr(), unit_length);
#endif
    

    // 2 - receiver: generate the inputs according to the choice bits.
    octet *seed_receiver = new octet[16];
    int starting_length = 4;
    for(int i=0; i<16; i++) seed_receiver[i] = os[1].get_data()[i+starting_length];
    G.SetSeed(seed_receiver);

#ifdef DEBUG_OUTPUT
    std::cerr << "os[1] value: " << std::endl;
    print_octet_stream_hex(os[1].get_data(), os[1].get_length());
    std::cerr << "seed receiver" << std::endl;
    print_octet_stream_hex(seed_receiver, 16);
#endif

    for(int i=0; i<nOT; i++){
        for(size_t j=0; j<unit_length; j++) {
            for(size_t k = 0; k < 8; k++){
                receiver_outputs[i].set_bit(j*8+k, (G.get_uchar() & 1) ^ receiver_inputs[i]);
            }
        }
    }

#ifdef DEBUG_OUTPUT
    std::cerr << "receiver outputs - " << std::endl;
    for(int i=0; i<nOT; i++) print_octet_stream_hex(receiver_outputs[i].get_ptr(), unit_length);
#endif

    // // debug - check hashs.
    // for (int i = 0; i < nOT; i++)
    // {
    //     if (ot_role & RECEIVER)
    //         hash_with_id(receiver_outputs.at(i), i);
    //     if (ot_role & SENDER)
    //         for (int j = 0; j < 2; j++)
    //             hash_with_id(sender_inputs.at(i).at(j), i);
    // }    
}

template <class T, class U>
void BaseOT::exec_base_tee(bool new_receiver_inputs)
{
    size_t len;
    vector<octetStream> os(2);
    PRNG G;
    G.ReSeed();

    T sender;
    U receiver;

    size_t unit_length = sender_inputs[0][0].size_bytes(); // 16 bytes

    os[0].reset_write_head();
    os[1].reset_write_head();

    // set the receiver inputs and the sender inputs.
    // sender sends the inputs to receivers and receiver it self selects.
    if (ot_role & RECEIVER)
    {   
        if(new_receiver_inputs){
            for(int i=0; i<nOT; i++){
                receiver_inputs[i] = G.get_uchar() & 1;
            }
        }
        for(int i=0; i<nOT; i++){
            for(size_t j=0; j<unit_length; j++) sender_inputs[i][0].set_byte(j, G.get_uchar());
            G.ReSeed();
            for(size_t j=0; j<unit_length; j++) sender_inputs[i][1].set_byte(j, G.get_uchar());
        }
    }

#ifdef DEBUG_OUTPUT 
    // check sender inputs.
    std::cerr << "sender inputs 1: " << std::endl;
    for(int i=0; i<nOT; i++){
        print_octet_stream_hex(sender_inputs[i][0].get_ptr(), unit_length);   
    }
    for(int i=0; i<nOT; i++){
        print_octet_stream_hex(sender_inputs[i][1].get_ptr(), unit_length);
    }
    std::cerr << std::endl;
#endif

    if (ot_role & RECEIVER)
    {

        os[0].store_bytes(receiver_inputs.get_ptr(), receiver_inputs.size_bytes());

#ifdef DEBUG_OUTPUT
        std::cerr << "receiver inputs: " << std::endl;
        print_octet_stream_hex(receiver_inputs.get_ptr(), receiver_inputs.size_bytes());
        std::cerr << std::endl;
        print_octet_stream_hex(os[0].get_data(), os[0].get_length());
        std::cerr << std::endl;
#endif
        P->send_receive_player(os); // exchange the information os[0] with os[1].
    }

    // the server choose the value according to the choice bit and sends to the receiver.
    if (ot_role & SENDER)
    {

// // both the sender save the receivers inputs in os[1], set their own inputs in os[0].
// #ifdef DEBUG_OUTPUT
//         print_octet_stream_hex(os[1].get_data(), os[1].get_length());
//         print_octet_stream_hex(os[0].get_data(), os[0].get_length());
// #endif
        
        // set the corresponding valur based on os[1] bits, and save it in os[0].
        size_t stream_length = unit_length * nOT;
        octet *target_oct = new octet[stream_length];

        int starting_length = 4;
        for (int i = 0; i < nOT; i++)
        {
            int byte = i / 8 + starting_length;
            int bit_loc = i % 8;
            int choice = (int)os[1].get_data()[byte] >> bit_loc & 1;

#ifdef DEBUG_OUTPUT
    std::cerr << "choice: " << choice << std::endl;
#endif
            // choice = 1;
            std::copy(sender_inputs[i][choice].get_ptr(), sender_inputs[i][choice].get_ptr() + unit_length, (target_oct + i * unit_length));
        }
        os[0].reset_read_head();
        os[0].reset_write_head();
        os[1].reset_read_head();
        os[1].reset_write_head();
        os[0].store_bytes(target_oct, stream_length);

#ifdef DEBUG_OUTPUT
        std::cerr << "extracted inputs: " << std::endl;
        print_octet_stream_hex(target_oct, stream_length);
        std::cerr << std::endl;
#endif

        P->send_receive_player(os);
    }

    // the receiver sets the received value to receiver_outputs.
    if (ot_role & RECEIVER)
    {
        int starting_length = 4;
        for (int i = 0; i < nOT; i++)
        {
            octet *target_oct = new octet[unit_length];
            size_t starting_point = i+starting_length;
            std::copy(os[1].get_data() + starting_point * unit_length, os[1].get_data() + (starting_point + 1) * unit_length, target_oct);
            for (size_t j = 0; j < unit_length; j++)
            {
                receiver_outputs[i].set_byte(j, os[1].get_data()[i * unit_length + starting_length + j]);
            }
        }
    }
}

// See https://eprint.iacr.org/2015/267.pdf
template <class T, class U>
void BaseOT::exec_base(bool new_receiver_inputs)
{
    int i, j, k;
    size_t len;
    PRNG G;
    G.ReSeed();

    vector<octetStream> os(2);
    T sender;
    U receiver;

    // std::cerr << "INVOKE THIS IN THIS BASE-OT FUNCTION" << std::endl;

    unsigned char S_pack[PACKBYTES];
    unsigned char Rs_pack[2][4 * PACKBYTES];
    unsigned char sender_keys[2][4][HASHBYTES];
    unsigned char receiver_keys[4][HASHBYTES];
    unsigned char cs[4];

    if (ot_role & SENDER)
    {
        // Sample a and compute A=g^a
        sender_genS(&sender, S_pack);
        // Send A
        os[0].store_bytes(S_pack, sizeof(S_pack));
    }
    send_if_ot_sender(P, os, ot_role);

    if (ot_role & RECEIVER)
    {
        // Receive A
        os[1].get_bytes((octet *)receiver.S_pack, len);
        if (len != HASHBYTES)
        {
            cerr << "Received invalid length in base OT\n";
            exit(1);
        }

        // Process A
        receiver_procS(&receiver);
        receiver_maketable(&receiver);
    }

    os[0].reset_write_head();

    for (i = 0; i < nOT; i += 4)
    {
        if (ot_role & RECEIVER)
        {
            for (j = 0; j < 4 and (i + j) < nOT; j++)
            {
                // Process choice bits
                if (new_receiver_inputs)
                    receiver_inputs[i + j] = G.get_uchar() & 1;
                cs[j] = receiver_inputs[i + j].get();
            }
            // Compute B
            receiver_rsgen(&receiver, Rs_pack[0], cs);
            // Send B
            os[0].store_bytes(Rs_pack[0], sizeof(Rs_pack[0]));
            // Compute k_R
            receiver_keygen(&receiver, receiver_keys);

            // Copy keys to receiver_outputs
            for (j = 0; j < 4 and (i + j) < nOT; j++)
            {
                for (k = 0; k < AES_BLK_SIZE; k++)
                {
                    receiver_outputs[i + j].set_byte(k, receiver_keys[j][k]);
                }
            }

#ifdef BASE_OT_DEBUG
            for (j = 0; j < 4; j++)
                for (k = 0; k < AES_BLK_SIZE; k++)
                {
                    printf("%4d-th receiver key:", i + j);
                    for (k = 0; k < HASHBYTES; k++)
                        printf("%.2X", receiver_keys[j][k]);
                    printf("\n");
                }

            printf("\n");
#endif
        }
    }

    send_if_ot_receiver(P, os, ot_role);

    for (i = 0; i < nOT; i += 4)
    {
        if (ot_role & SENDER)
        {
            // Receive B
            os[1].get_bytes((octet *)Rs_pack[1], len);
            if (len != sizeof(Rs_pack[1]))
            {
                cerr << "Received invalid length in base OT\n";
                exit(1);
            }
            // Compute k_0 and k_1
            sender_keygen(&sender, Rs_pack[1], sender_keys);

            // Copy 128 bits of keys to sender_inputs
            for (j = 0; j < 4 and (i + j) < nOT; j++)
            {
                for (k = 0; k < AES_BLK_SIZE; k++)
                {
                    sender_inputs[i + j][0].set_byte(k, sender_keys[0][j][k]);
                    sender_inputs[i + j][1].set_byte(k, sender_keys[1][j][k]);
                }
            }
        }
#ifdef BASE_OT_DEBUG
        for (j = 0; j < 4; j++)
        {
            if (ot_role & SENDER)
            {
                printf("%4d-th sender keys:", i + j);
                for (k = 0; k < HASHBYTES; k++)
                    printf("%.2X", sender_keys[0][j][k]);
                printf(" ");
                for (k = 0; k < HASHBYTES; k++)
                    printf("%.2X", sender_keys[1][j][k]);
                printf("\n");
            }
        }

        printf("\n");
#endif
    }

    // std::cerr << "sender inputs 0" << std::endl;
    // for (int i = 0; i < nOT; i++)
    // {
    //     print_octet_stream_hex(sender_inputs[i][0].get_ptr(), sender_inputs[i][0].size_bytes());
    // }

    // Hash with counter to avoid collisions
    for (int i = 0; i < nOT; i++)
    {
        if (ot_role & RECEIVER)
            hash_with_id(receiver_outputs.at(i), i);
        if (ot_role & SENDER)
            for (int j = 0; j < 2; j++)
                hash_with_id(sender_inputs.at(i).at(j), i);
    }

    // Set PRG seeds
    set_seeds();
}

void BaseOT::hash_with_id(BitVector &bits, long id)
{
    assert(bits.size_bytes() >= AES_BLK_SIZE);
    Hash hash;
    hash.update(bits.get_ptr(), bits.size_bytes());
    hash.update(&id, sizeof(id));
    hash.final(bits.get_ptr(), bits.size_bytes());
}

void BaseOT::set_seeds()
{
    for (int i = 0; i < nOT; i++)
    {
        // Set PRG seeds
        if (ot_role & SENDER)
        {
            G_sender[i][0].SetSeed(sender_inputs[i][0].get_ptr());
            G_sender[i][1].SetSeed(sender_inputs[i][1].get_ptr());
        }
        if (ot_role & RECEIVER)
        {
            G_receiver[i].SetSeed(receiver_outputs[i].get_ptr());
        }
    }
    extend_length();
}

void BaseOT::extend_length()
{
    for (int i = 0; i < nOT; i++)
    {
        if (ot_role & SENDER)
        {
            sender_inputs[i][0].randomize(G_sender[i][0]);
            sender_inputs[i][1].randomize(G_sender[i][1]);
        }
        if (ot_role & RECEIVER)
        {
            receiver_outputs[i].randomize(G_receiver[i]);
        }
    }
}

void BaseOT::check()
{
    vector<octetStream> os(2);
    BitVector tmp_vector(8 * AES_BLK_SIZE);

    for (int i = 0; i < nOT; i++)
    {
        if (ot_role == SENDER)
        {
            // send both inputs over
            sender_inputs[i][0].pack(os[0]);
            sender_inputs[i][1].pack(os[0]);
            P->send(os[0]);
        }
        else if (ot_role == RECEIVER)
        {
            P->receive(os[1]);
        }
        else
        {
            // both sender + receiver
            sender_inputs[i][0].pack(os[0]);
            sender_inputs[i][1].pack(os[0]);
            P->send_receive_player(os);
        }
        if (ot_role & RECEIVER)
        {
            tmp_vector.unpack(os[1]);

            if (receiver_inputs[i] == 1)
            {
                tmp_vector.unpack(os[1]);
            }
            if (!tmp_vector.equals(receiver_outputs[i]))
            {
                cerr << "Incorrect OT\n";
                exit(1);
            }
        }
        os[0].reset_write_head();
        os[1].reset_write_head();
    }
}

void FakeOT::exec_base(bool new_receiver_inputs)
{
    insecure("base OTs");
    PRNG G;
    G.ReSeed();
    vector<octetStream> os(2);
    vector<BitVector> bv(2, 128);

    if ((ot_role & RECEIVER) && new_receiver_inputs)
    {
        for (int i = 0; i < nOT; i++)
            // Generate my receiver inputs
            receiver_inputs[i] = G.get_uchar() & 1;
    }

    if (ot_role & SENDER)
        for (int i = 0; i < nOT; i++)
            for (int j = 0; j < 2; j++)
            {
                sender_inputs[i][j].randomize(G);
                sender_inputs[i][j].pack(os[0]);
            }

    send_if_ot_sender(P, os, ot_role);

    if (ot_role & RECEIVER)
        for (int i = 0; i < nOT; i++)
        {
            for (int j = 0; j < 2; j++)
                bv[j].unpack(os[1]);
            receiver_outputs[i] = bv[receiver_inputs[i].get()];
        }

    set_seeds();
}
