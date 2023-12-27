#ifndef _PROCESSOR_LOG_
#define _PROCESSOR_LOG_

#include <stack>
#include <iostream>

#include "Processor/SubProcessorLog.hpp"
#include "Processor/Processor.h"
#include "Processor/LogFileManager.h"

using namespace std;

template<class sint, class sgf2n>
class ProcessorLog {

public:
    // file manager in singleton mode
    LogFileManager<sint, sgf2n> *log_file_manager;
    
    // Processor ptr
    Processor<sint, sgf2n> *processor;

    // PC of Processor
    unsigned int PC_log;

    // Target to dump Rergisters of Processor
    // stack<long> stacki_log;
    // CheckVector<long> Ci_log;

    SubProcessorLog<sint, sgf2n, sint>* Procp_log;
    SubProcessorLog<sint, sgf2n, sgf2n>*  Proc2_log;
    OnlineOptions opts;

    ProcessorLog(Processor<sint, sgf2n> *processor);

    void dump_processorlog();

    void dump_PC();

    void dump_stacki();

    void dump_Ci();

    void dump_online_options();

    void dump_procp(SubProcessor<sint> *subprocesssor);

    void dump_proc2(SubProcessor<sgf2n> *subprocesssor);

};
#endif