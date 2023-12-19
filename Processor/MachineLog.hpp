#include "MachineLog.h"
#include "Processor/Machine.h"

template <class sint, class sgf2n>
MachineLog<sint, sgf2n>::MachineLog(Machine<sint, sgf2n> *machine) {
    this -> machine = machine;
    outf = nullptr;
    inf = nullptr;
}

template <class sint, class sgf2n>
void MachineLog<sint, sgf2n>::dump_machinelog(ofstream outf) {
    this -> outf = outf;
    outf << "MachineLog" << endl;
    dump_Memory("M2", machine -> M2);
    dump_Memory("Mp", machine -> Mp);
    dump_Memory("Mi", machine -> Mi); 
}

template <class sint, class sgf2n>
template <class T>
void MachineLog<sint, sgf2n>::dump_Memory(string memory_type, Memory<T> *target_memory) {
    outf << "Memory " << memory_type << endl;
    dump_MemoryPart("MS", target_memory -> MS);
    dump_MemoryPart("MC", target_memory -> MC);
}


template <class sint, class sgf2n>
template <class T>
void MachineLog<sint, sgf2n>::dump_MemoryPart(string memorypart_type, MemoryPart<T> *target_memorypart) {
    outf << "MemoryPart " << memorypart_type << endl; 
    outf << "size" << " " << target_memorypart -> size() << endl;
    for (int i = 0; i < target_memorypart -> size(); i++) {
        cout << (*target_memorypart)[i] << " ";
    }
}
