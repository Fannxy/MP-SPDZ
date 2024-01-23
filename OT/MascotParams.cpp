/*
 * TripleMachine.cpp
 *
 */

#include "MascotParams.h"

MascotParams::MascotParams()
{
    generateMACs = true;
    amplify = true;
    check = true;
    correlation_check = true;
    generateBits = false;
#ifdef TEE_RANDOM_OT
    // std::cerr << "Using TEE random OT\n" << std::endl;
    use_extension = false;
#else
    // std::cerr << "Using regular random OT\n" << std::endl;
    use_extension = true;
#endif
    fewer_rounds = false;
    fiat_shamir = false;
    timerclear(&start);
}

void MascotParams::set_passive()
{
    generateMACs = amplify = check = correlation_check = false;
}
