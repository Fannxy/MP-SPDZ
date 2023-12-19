#include "Processor/ProcessorLog.h"

template <class sint, class sgf2n>
ProcessorLog<sint, sgf2n>::ProcessorLog(Processor<sint, sgf2n> *processor) {
    inf = nullptr;
    outf = nullptr;
    this -> processor = processor;
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_processorlog(ofstream outf) {
    this -> outf = outf;
    outf << "Processor " << processor -> thread_num;
    dump_PC();
    dump_stacki();
    dump_Ci();
    dump_subprocessor(0, processor -> Proc2);   // first param to get member's name
    dump_subprocessor(1, processor -> Procp);   // 0 for Proc2, 1 for Procp
    // dump_online_options(); TODO
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_PC() {
    outf << "PC" << endl;
    outf << processor -> PC;
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_stacki() {
    outf << "stacki" << endl;
    outf << "size" << " " << (processor -> stacki).size() << endl; 
    for (int i = 0; i < (processor -> stacki).size(); i++) {
        outf << (processor -> stacki)[i] << " ";
    }
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_Ci() {
    outf << "Ci" << endl;
    outf << "size" << " " << (processor -> Ci).size() << endl;
    for (int i = 0; i < (processor -> Ci).size(); i++) {
        outf << (processor -> Ci)[i] << " ";
    }
}

template <class sint, class sgf2n>
void ProcessorLog<sint, sgf2n>::dump_online_options() {
    throw runtime_error(
        "^^^^^^^^^^^^^^^^^^^^No Implemented^^^^^^^^^^^^^^^^^^^^");
}

template <class sint, class sgf2n>
template <class T>
void ProcessorLog<sint, sgf2n>::dump_subprocessor(int subprocessor_type, SubProcessor<T> *subprocesssor) {
    if (! subprocessor_type) {
        this -> Procp_log = &(SubProcessorLog(subprocesssor));
        (this -> Procp_log) -> dump_subprocessorlog(outf);
    } else {
         this -> Proc2_log = &(SubProcessorLog(subprocesssor));
        (this -> Proc2_log) -> dump_subprocessorlog(outf);
    } 
}