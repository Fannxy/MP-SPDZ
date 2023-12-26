#include "Processor/Log.h"
#include "Processor/Machine.h"
#include "Processor/Processor.h"
#include "Processor/MachineLog.hpp"
#include "Processor/LogFileManager.hpp"
#include "Processor/ProcessorLog.hpp"

#include <ctime>
#include <fstream>
#include <iostream>
#include <cstring>
#include <cstdlib>

template <class sint, class sgf2n>
Log<sint, sgf2n>::Log(Processor<sint, sgf2n> *processor) {
    this -> processor = processor;
    this -> log_file_manager = &LogFileManager<sint, sgf2n>::getInstance(processor);
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_time() {
    time_t rawtime;
    struct tm *ptminfo;
    time(&rawtime);
    ptminfo = localtime(&rawtime);
    LOGOUT("time\n", ptminfo -> tm_year + 1900, " ", ptminfo -> tm_mon + 1, " ");
    LOGOUT(ptminfo -> tm_mday, " ", ptminfo -> tm_hour, " ");
    LOGOUT(ptminfo -> tm_min, " ", ptminfo -> tm_sec, "\n");
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_basic_info(int id_log) {
    LOGOUT("id\n", id_log, "\n");
    LOGOUT("player_no\n", ((this -> processor) -> P).my_num(), "\n");
    LOGOUT("nthreads\n", ((this -> processor)->machine).nthreads, "\n");
    dump_time();
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_machine_log(Processor<sint, sgf2n> *processor) {
    machine_log = new MachineLog(processor);
    this -> machine_log = machine_log;
    (this -> machine_log) -> dump_machinelog();
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_current_processor_log(Processor<sint, sgf2n> *processor) {
    ProcessorLog curr_processorlog(processor);
    (this -> processor_logs).push_back(&curr_processorlog);
    curr_processorlog.dump_processorlog();
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_processor_logs() {
    throw runtime_error(
            "^^^^^^^^^^^^^^^^^^^^No implemented for multi-threads circumstances^^^^^^^^^^^^^^^^^^^^");
    return;
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_log() {
    int id_log = 0;
    (this -> log_file_manager) -> generate_log_title_file(id_log);
    (this -> log_file_manager) -> generate_log_file(id_log);
    dump_basic_info(id_log);
    dump_machine_log(processor);
    if (((this -> processor)->machine).nthreads == 1) {
       dump_current_processor_log((this -> processor));
    } else {
        dump_processor_logs();
    }
    (this -> log_file_manager) -> end_generate_log_file();
    // Any Other TODO?
    return;
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::read_log() {
    throw runtime_error(
        "^^^^^^^^^^^^^^^^^^^^No implemented for reloading^^^^^^^^^^^^^^^^^^^^");
}