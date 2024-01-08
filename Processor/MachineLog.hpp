#include "MachineLog.h"
#include "Processor/Machine.h"

// ------------------ MemoryLog ------------------
template <class sint, class sgf2n, class T>
void  MemoryLog<sint, sgf2n, T>::generate_Memory(Memory<T> *target_memory) {
            this->generate_MS(&(target_memory -> MS));
            this->generate_MC(&(target_memory -> MC));
        }

template <class sint, class sgf2n, class T>
void MemoryLog<sint, sgf2n, T>::generate_MS(MemoryPart<T> *target_memorypart) {
    MS_log.resize(target_memorypart -> size());
    for (size_t i = 0; i < target_memorypart -> size(); i++) {
        MS_log[i] = (*target_memorypart)[i];
    }
}

template <class sint, class sgf2n, class T>
void MemoryLog<sint, sgf2n, T>::generate_MC(MemoryPartImpl<typename T::clear, CheckVector> *target_memoryartimpl) {
    MC_log.resize(target_memoryartimpl -> size());
    for (size_t i = 0; i < target_memoryartimpl -> size(); i++) {
        MC_log[i] = (*target_memoryartimpl)[i];
    }
}

// ------------------ MachineLog ------------------
template <class sint, class sgf2n>
MachineLog<sint, sgf2n>::MachineLog(Processor<sint, sgf2n> *processor) {
    this -> machine = &(processor ->machine);
}

template <class sint, class sgf2n>
void MachineLog<sint, sgf2n>::generate_machinelog() {
    M2_log.generate_Memory(&(machine -> M2));
    Mp_log.generate_Memory(&(machine -> Mp));
    Mi_log.generate_Memory(&(machine -> Mi));
}

