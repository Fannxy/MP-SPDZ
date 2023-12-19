#include "Processor/SubProcessorLog.h"
#include "Processor/Processor.h"
#include <iostream>

template <class T>
SubProcessorLog<T>::SubProcessorLog(SubProcessor<T> *subprocessor) {
    inf = nullptr;
    outf = nullptr;
    this -> subprocessor = subprocessor;
} 

template <class T>
void SubProcessorLog<T>::dump_subprocessorlog(ofstream outf) {
    this -> outf = outf;
    outf << "subprocessor" << endl; 
    dump_C();
    dump_S();
}

template <class T>
void SubProcessorLog<T>::dump_C() {
    outf << "C" << endl;
    outf << "size" << " " << (subprocessor->C).size() << endl;
    for (int i = 0; i < (subprocessor->C).size(); i++) {
        outf << (subprocessor->C)[i] << " ";
    }
}

template <class T>
void SubProcessorLog<T>::dump_S() {
    outf << "S" << endl;
    outf << "size" << " " << (subprocessor->S).size() << endl;
    for (int i = 0; i < (subprocessor->S).size(); i++) {
        outf << (subprocessor->S)[i] << " ";
    }
}