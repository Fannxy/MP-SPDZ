#ifndef _PROCESSOR_LOG_
#define _PROCESSOR_LOG_

#include <stack>
#include <iostream>

#include "Processor/SubProcessorLog.h"
#include "Processor/Processor.h"

using namespace std;

template<class sint, class sgf2n>
class ProcessorLog {

public:
    // target file && source file
    ofstream outf;
    ifstream inf;
    
    // Processor ptr
    Processor<sint, sgf2n> *processor;

    // PC of Processor
    unsigned int PC_log;

    // Target to dump Rergisters of Processor
    // stack<long> stacki_log;
    // CheckVector<long> Ci_log;

    SubProcessorLog<sint>* Procp_log;
    SubProcessorLog<sgf2n>*  Proc2_log;
    OnlineOptions opts;

    ProcessorLog(Processor<sint, sgf2n> *processor);

    void dump_processorlog(ofstream outf);

    void dump_PC();

    void dump_stacki();

    void dump_Ci();

    void dump_online_options();

    template <class T>
    void dump_subprocessor(int subprocessor_type, SubProcessor<T> *subprocesssor);


};
#endif