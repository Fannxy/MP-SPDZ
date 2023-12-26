#ifndef _MACHINE_LOG_
#define _MACHINE_LOG_

#include <iostream>
#include "Processor/Memory.h"

using namespace std;

template<class sint, class sgf2n>
class MachineLog {

public:
    // target file && source file
    ofstream outf;
    ifstream inf;

    // Mahcine_ptr
    Machine<sint, sgf2n> *machine;

    // Target to dump Memory of Machine
    // Memory<sgf2n> M2_log;
    // Memory<sint> Mp_log;
    // Memory<Integer> Mi_log;

    MachineLog(Machine<sint, sgf2n> *machine);

    void dump_machinelog();

    template <class T>
    void dump_Memory(string memory_type, Memory<T> *target_memory);

    template <class T>
    void dump_MemoryPart(string memorypart_type, MemoryPart<T> *target_memorypart);

};
#endif