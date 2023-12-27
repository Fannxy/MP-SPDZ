#ifndef _SUBPROCESSOR_LOG_
#define _SUBPROCESSOR_LOG_

#include "Tools/CheckVector.h"
#include "Processor/Processor.h"
#include "Processor/LogFileManager.h"
#include <iostream>

using namespace std;


template <class sint, class sgf2n, class T>
class SubProcessorLog {
public:
    // file manager in singleton mode
    LogFileManager<sint, sgf2n> *log_file_manager;

    // SubProcessor ptr
    SubProcessor<T> *subprocessor; 

    // Target to dump Registers of SubProcessor
    CheckVector<typename T::clear> C_log;
    CheckVector<T> S_log;
    
    SubProcessorLog(SubProcessor<T> *subprocessor, Processor<sint, sgf2n> *processor);

    void dump_subprocessorlog();

    void dump_C();

    void dump_S();

};
#endif