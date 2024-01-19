#include "Processor/LogFileManager.h"

#include <fstream>
#include <iostream>
#include <string>
#include <utility>

template <class sint, class sgf2n>
void LogFileManager::dump_machine_log(Log<sint, sgf2n>* log) {
    dump_to_file("Memory type ", "M2", "\n");
    dump_memory_log(M2_LOG);
    dump_to_file("Memory type ", "Mp" , "\n");
    dump_memory_log(MP_LOG);
    dump_to_file("Memory type ", "Mi", "\n");
    dump_memory_log(MI_LOG);
}

template <class sint, class sgf2n, class T>
void LogFileManager::dump_memory_log(MemoryLog<sint, sgf2n, T> memory_log) {
    dump_to_file("MemoryPart type ", "MS", "\n");
    dump_to_file("size ", MS_LOG.size(), "\n");
    for (size_t i = 0; i < MS_LOG.size(); i++) {
        dump_to_file(MS_LOG[i], " ");
    }
    dump_to_file("\n");

    dump_to_file("MemoryPart type ", "MC", "\n");
    dump_to_file("size ", MC_LOG.size(), "\n");
    for (size_t i = 0; i < MC_LOG.size(); i++) {
        dump_to_file(MC_LOG[i], " ");
    }
    dump_to_file("\n");
}


template <class sint, class sgf2n>
void LogFileManager::dump_stacki(ProcessorLog<sint, sgf2n>* processor_log) {
    dump_to_file("size ", STACKI_LOG.size(), "\n");
    while (! STACKI_LOG.empty()) {
        dump_to_file(STACKI_LOG.top(), " ");
        STACKI_LOG.pop();
    }
    dump_to_file("\n");
}

template <class sint, class sgf2n>
void LogFileManager::dump_Ci(ProcessorLog<sint, sgf2n>* processor_log) {
    dump_to_file("size ", CI_LOG.size(), "\n");
    for (size_t i = 0; i < CI_LOG.size(); i++) {
        dump_to_file(CI_LOG[i], " ");
    }
    dump_to_file("\n");
}

template <class sint, class sgf2n, class T>
void LogFileManager::dump_subprocessor(SubProcessorLog<sint, sgf2n, T>* subprocessor_log) {
    dump_to_file("C\n");
    dump_to_file("size ", C_LOG.size(), "\n");
    for (size_t i = 0; i < C_LOG.size(); i++) {
        dump_to_file(C_LOG[i], " ");
    }
    dump_to_file("\n");

    dump_to_file("S\n");
    dump_to_file("size ", S_LOG.size(), "\n");
    for (size_t i = 0; i < S_LOG.size(); i++) {
        dump_to_file(S_LOG[i], " ");
    }
    dump_to_file("\n");
}

template <class sint, class sgf2n>
void LogFileManager::dump_processor_log(ProcessorLog<sint, sgf2n>* processor_log) {
    dump_to_file("PC\n");
    dump_to_file(processor_log -> PC_log, "\n");
    dump_to_file("stacki (with top at first)\n");
    dump_stacki(processor_log);
    dump_to_file("Ci\n");
    dump_Ci(processor_log);
    dump_to_file("Procp\n");
    dump_subprocessor(processor_log -> procp_log);
    dump_to_file("Proc2\n");
    dump_subprocessor(processor_log -> proc2_log);
    // TODO dump_online_options();
}

template <class sint, class sgf2n>
void LogFileManager::dump_processor_logs(Log<sint, sgf2n>* log) {
    dump_to_file("size ", PROCESSOR_LOGS.size(), "\n");
    for (size_t i = 0; i < PROCESSOR_LOGS.size(); i++) {
        dump_to_file("Processor ", i, "\n"); // TODO: Now can only handle circumstance {0}.
        dump_processor_log(PROCESSOR_LOGS[i]);
    }
}

// Assume all vars from processor here will not be changed.
// OR to throw all theses vars into log, and detach log with template and processor
template <class sint, class sgf2n>
void LogFileManager::prepare_dump_log(Processor<sint, sgf2n> *processor) {
    player_num = (processor -> P).my_num();
    player_nthreads = (processor -> machine).nthreads;
    generate_log_title_file();
    generate_log_file();
}

// Producer's func to consume source
template <class sint, class sgf2n>
void* LogFileManager::dump_entry(void* arg) {
    pair<LogFileManager*, Log<sint, sgf2n>*>* outer_obj = (pair<LogFileManager*, Log<sint, sgf2n>*>*)arg;
    LogFileManager* obj_1 = outer_obj -> first;
    Log<sint, sgf2n>* obj_2 = outer_obj -> second;
    obj_1 -> dump_thread(obj_2);
    return nullptr;
}

template <class sint, class sgf2n>
void LogFileManager::dump_thread(Log<sint, sgf2n>* log) {
    prepare_dump_log(log -> processor);
    open_log_file();
    dump_basic_info();
    dump_to_file("MachineLog\n");
    dump_machine_log(log);
    dump_to_file("ProcessorLogs\n");
    dump_to_file("Processors\n");
    dump_processor_logs(log);
    close_log_file();
    Processor<sint, sgf2n>* cur_processor = log -> processor;
    delete log;
    cur_processor -> workers_status[worker_id] = IDLE;
    pthread_cond_signal(&(cur_processor -> finish_work_signal));
    // Any Other TODO?
}
