#include "Processor/SubProcessorLog.h"
#include "Processor/Processor.h"
#include <iostream>

template<class sint, class sgf2n, class T>
SubProcessorLog<sint, sgf2n, T>::SubProcessorLog(SubProcessor<T> *subprocessor, Processor<sint, sgf2n> *processor) {
    this -> subprocessor = subprocessor;
    this -> log_file_manager = &LogFileManager<sint, sgf2n>::getInstance(processor);
} 

template<class sint, class sgf2n, class T>
void SubProcessorLog<sint, sgf2n, T>::dump_subprocessorlog() {
    LOGOUT("subprocessor\n"); 
    dump_C();
    dump_S();
}

template<class sint, class sgf2n, class T>
void SubProcessorLog<sint, sgf2n, T>::dump_C() {
    LOGOUT("C\n");
    LOGOUT("size ", (subprocessor->get_C()).size(), "\n");
    for (unsigned long i = 0; i < (subprocessor->get_C()).size(); i++) {
        LOGOUT(subprocessor->get_C()[i], " ");
    }
    LOGOUT("\n");
}

template<class sint, class sgf2n, class T>
void SubProcessorLog<sint, sgf2n, T>::dump_S() {
    LOGOUT("S\n");
    LOGOUT("size ", (subprocessor->get_S()).size(), "\n");
    for (unsigned long i = 0; i < (subprocessor->get_S()).size(); i++) {
        LOGOUT((subprocessor->get_S())[i], " ");
    }
    LOGOUT("\n");
}