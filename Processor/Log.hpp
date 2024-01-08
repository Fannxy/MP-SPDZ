#include "Processor/Log.h"
#include "Processor/Machine.h"
#include "Processor/Processor.h"
#include "Processor/MachineLog.hpp"
#include "Processor/ProcessorLog.hpp"

#include <ctime>
#include <fstream>
#include <iostream>
#include <cstring>
#include <cstdlib>

template <class sint, class sgf2n>
Log<sint, sgf2n>::Log(Processor<sint, sgf2n> *processor) {
    this -> processor = processor;
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::generate_machine_log(Processor<sint, sgf2n> *processor) {
    machine_log = new MachineLog(processor);
    this -> machine_log = machine_log;
    (this -> machine_log) -> generate_machinelog();
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::generate_current_processor_log(Processor<sint, sgf2n> *processor) {
    ProcessorLog curr_processorlog(processor);
    (this -> processor_logs).push_back(curr_processorlog);
    (this -> processor_logs)[(this -> processor_logs).size() - 1].generate_processorlog();
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::generate_processor_logs() {
    throw runtime_error(
            "^^^^^^^^^^^^^^^^^^^^No implemented for multi-threads circumstances^^^^^^^^^^^^^^^^^^^^");
    return;
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::generate_log() {
    generate_machine_log(processor);
    if (((this -> processor)->machine).nthreads == 1) {
       generate_current_processor_log((this -> processor));
    } else {
        generate_processor_logs();
    }
    return;
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::read_log() {
    throw runtime_error(
        "^^^^^^^^^^^^^^^^^^^^No implemented for reloading^^^^^^^^^^^^^^^^^^^^");
}

