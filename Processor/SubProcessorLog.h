#ifndef _SUBPROCESSOR_LOG_
#define _SUBPROCESSOR_LOG_

#include "Tools/CheckVector.h"
#include "Processor/Processor.h"
#include <iostream>

using namespace std;


template <class T>
class SubProcessorLog {
    // target file && source file
    ofstream outf;
    ifstream inf;

    // SubProcessor ptr
    SubProcessor<T> *subprocessor; 

    // Target to dump Registers of SubProcessor
    CheckVector<typename T::clear> C_log;
    CheckVector<T> S_log;
    
    SubProcessorLog(SubProcessor<T> *subprocessor);

    void dump_subprocessorlog(ofstream outf);

    void dump_C();

    void dump_S();

};
#endif