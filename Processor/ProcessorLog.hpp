#include "Processor/ProcessorLog.h"
#include "Math/Integer.h"
#include <stack>

template <class sint, class sgf2n>
ProcessorLog<sint, sgf2n>::ProcessorLog(Processor<sint, sgf2n> *processor) {
    this -> processor = processor;
    this -> log_file_manager = &LogFileManager<sint, sgf2n>::getInstance(processor);
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_processorlog() {
    LOGOUT("Processor ", processor -> thread_num, "\n");
    dump_PC();
    dump_stacki();
    dump_Ci();
    dump_procp(&(processor -> Procp));
    dump_proc2(&(processor -> Proc2));
    // dump_online_options(); TODO
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_PC() {
    LOGOUT("PC\n");
    LOGOUT(processor -> PC, "\n");
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_stacki() {
    LOGOUT("stacki with top at first\n");
    stack<Integer> stacki_cp = processor -> get_stack();
    LOGOUT("size ", stacki_cp.size(), "\n");
    while (! stacki_cp.empty()) {
        LOGOUT(stacki_cp.top(), " ");
        stacki_cp.pop();
    }
    LOGOUT("\n");
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_Ci() {
    LOGOUT("Ci\n");
    LOGOUT("size ", (processor -> get_Ci()).size(), "\n");
    for (unsigned long i = 0; i < (processor -> get_Ci()).size(); i++) {
        LOGOUT((processor -> get_Ci())[i], " ");
    }
    LOGOUT("\n");
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_online_options() {
    throw runtime_error(
        "^^^^^^^^^^^^^^^^^^^^No Implemented^^^^^^^^^^^^^^^^^^^^");
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_procp(SubProcessor<sint> *subprocessor) {
    SubProcessorLog<sint, sgf2n, sint> procp_log = SubProcessorLog(subprocessor, processor);
    this -> Procp_log = &procp_log;
    procp_log.dump_subprocessorlog();
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_proc2(SubProcessor<sgf2n> *subprocessor) {
    SubProcessorLog<sint, sgf2n, sgf2n> proc2_log = SubProcessorLog(subprocessor, processor);
    this -> Proc2_log = &proc2_log;
    proc2_log.dump_subprocessorlog();
}