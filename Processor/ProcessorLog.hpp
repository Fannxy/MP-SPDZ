#include "Processor/ProcessorLog.h"
#include "Math/Integer.h"
#include <stack>

// -------------------------- SubProcessorLog --------------------------
template<class sint, class sgf2n, class T>
SubProcessorLog<sint, sgf2n, T>::SubProcessorLog(SubProcessor<T> *subprocessor) {
    this -> subprocessor = subprocessor;
} 

template<class sint, class sgf2n, class T>
void SubProcessorLog<sint, sgf2n, T>::generate_subprocessorlog() {
    this -> C_log = subprocessor -> get_C();
    this -> S_log = subprocessor -> get_S(); 
}

// -------------------------- ProcessorLog --------------------------
template <class sint, class sgf2n>
ProcessorLog<sint, sgf2n>::ProcessorLog(Processor<sint, sgf2n> *processor) {
    this -> processor = processor;
}

template <class sint, class sgf2n>
ProcessorLog<sint, sgf2n>::~ProcessorLog() {
    delete procp_log;
    delete proc2_log;
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::generate_processorlog() {
    this -> PC_log = processor -> PC;
    this -> stacki_log = processor -> get_stack();
    generate_Ci(); // get_Ci get & as return value
    generate_procp(&(processor -> Procp));
    generate_proc2(&(processor -> Proc2));
    // generate_online_options(); TODO
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::generate_online_options() {
    throw runtime_error(
        "^^^^^^^^^^^^^^^^^^^^No Implemented^^^^^^^^^^^^^^^^^^^^");
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::generate_procp(SubProcessor<sint> *subprocessor) {
    procp_log = new SubProcessorLog<sint, sgf2n, sint>(subprocessor);
    this -> procp_log = procp_log;
    procp_log -> generate_subprocessorlog();
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::generate_proc2(SubProcessor<sgf2n> *subprocessor) {
    proc2_log = new SubProcessorLog<sint, sgf2n, sgf2n>(subprocessor);
    this -> proc2_log = proc2_log;
    proc2_log -> generate_subprocessorlog();
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::generate_Ci() {
    CheckVector<Integer> Ci_cp = processor -> get_Ci();
    (this -> Ci_log).resize(Ci_cp.size());
    for (size_t i = 0; i < Ci_cp.size(); i++) {
        (this -> Ci_log)[i] = Ci_cp[i];
    }
}