#ifndef _MACHINE_LOG_
#define _MACHINE_LOG_

#include <iostream>
#include "Processor/Memory.h"
#include "Processor/Processor.h"

using namespace std;

template <class sint, class sgf2n, class T>
class MemoryLog {
public:

    // TODO: MS's type is decided by build function of the Class Memory(Memory.hpp)
    // Actually it is converted to MemoryImpl
    // default: 0
    MemoryPartImpl<T, CheckVector> MS_log;
    MemoryPartImpl<typename T::clear, CheckVector> MC_log;

    MemoryLog() {};

    void generate_Memory(Memory<T> *target_memory);

    void generate_MS(MemoryPart<T> *target_memorypart);

    void generate_MC(MemoryPartImpl<typename T::clear, CheckVector> *target_memoryartimpl);
};


template <class sint, class sgf2n>
class MachineLog {

public:
    // Mahcine_ptr
    Machine<sint, sgf2n> *machine;

    // Target to generate Memory of Machine
    MemoryLog<sint, sgf2n, sgf2n> M2_log;
    MemoryLog<sint, sgf2n, sint> Mp_log;
    MemoryLog<sint, sgf2n, Integer> Mi_log;

    MachineLog(Processor<sint, sgf2n> *processor);

    void generate_machinelog();
};
#endif