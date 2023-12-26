#ifndef _MACHINE_LOG_
#define _MACHINE_LOG_

#include <iostream>
#include "Processor/Memory.h"
#include "Processor/LogFileManager.h"
#include "Processor/Processor.h"

using namespace std;

#define LOGOUT(...) (this -> log_file_manager) -> dump_to_file(__VA_ARGS__)

template<class sint, class sgf2n>
class MachineLog {

public:
    // file manager in singleton mode
    LogFileManager<sint, sgf2n> *log_file_manager;

    // Mahcine_ptr
    Machine<sint, sgf2n> *machine;

    // Target to dump Memory of Machine
    // Memory<sgf2n> M2_log;
    // Memory<sint> Mp_log;
    // Memory<Integer> Mi_log;

    MachineLog(Processor<sint, sgf2n> *processor);

    void dump_machinelog();

    template <class T>
    void dump_Memory(string memory_type, Memory<T> *target_memory);

    template <class T>
    void dump_MemoryPart(string memorypart_type, MemoryPart<T> *target_memorypart);

};
#endif