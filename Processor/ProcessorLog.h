#ifndef _PROCESSOR_LOG_
#define _PROCESSOR_LOG_

#include <stack>
#include <iostream>

#include "Tools/CheckVector.h"
#include "Processor/Processor.h"

using namespace std;

template <class sint, class sgf2n, class T>
class SubProcessorLog {
public:
    // SubProcessor ptr
    SubProcessor<T> *subprocessor; 

    // Target to dump Registers of SubProcessor
    CheckVector<typename T::clear> C_log;
    CheckVector<T> S_log;
    
    SubProcessorLog(SubProcessor<T> *subprocessor);

    void generate_subprocessorlog();
};

template<class sint, class sgf2n>
class ProcessorLog {

public:
    // Processor ptr
    Processor<sint, sgf2n> *processor;

    // PC of Processor
    unsigned int PC_log;

    // Target to dump Rergisters of Processor
    stack<Integer> stacki_log;
    CheckVector<Integer> Ci_log;

    SubProcessorLog<sint, sgf2n, sint>* procp_log;
    SubProcessorLog<sint, sgf2n, sgf2n>*  proc2_log;
    OnlineOptions opts;

    ProcessorLog(Processor<sint, sgf2n> *processor);

    void generate_processorlog();

    void generate_online_options();

    void generate_procp(SubProcessor<sint> *subprocesssor);

    void generate_proc2(SubProcessor<sgf2n> *subprocesssor);

    void generate_Ci();

};
#endif