#include "MachineLog.h"
#include "Processor/Machine.h"

template <class sint, class sgf2n>
MachineLog<sint, sgf2n>::MachineLog(Processor<sint, sgf2n> *processor) {
    this -> machine = &(processor ->machine);
    this -> log_file_manager = &LogFileManager<sint, sgf2n>::getInstance(processor);
}

template <class sint, class sgf2n>
template <class T>
void MachineLog<sint, sgf2n>::dump_Memory(string memory_type, Memory<T> *target_memory) {
    LOGOUT("Memory type ", memory_type, "\n");
    (void) target_memory;
    dump_MemoryPart("MS", &(target_memory -> MS));
    dump_MemoryPart("MC", &(target_memory -> MC));
}

template <class sint, class sgf2n>
void MachineLog<sint, sgf2n>::dump_machinelog() {
    (this -> log_file_manager) -> dump_to_file("MachineLog\n");
    dump_Memory("M2", &(machine -> M2));
    dump_Memory("Mp", &(machine -> Mp));
    dump_Memory("Mi", &(machine -> Mi)); 
}

template <class sint, class sgf2n>
template <class T>
void MachineLog<sint, sgf2n>::dump_MemoryPart(string memorypart_type, MemoryPart<T> *target_memorypart) {
    LOGOUT("MemoryPart type ", memorypart_type, "\n");
    LOGOUT("size\n", target_memorypart->size(), "\n");
    for (size_t i = 0; i < target_memorypart -> size(); i++) {
        LOGOUT((*target_memorypart)[i], " ");
    }
    LOGOUT("\n");
}
