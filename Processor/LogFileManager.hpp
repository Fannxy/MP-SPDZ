#include "Processor/LogFileManager.h"

#include <fstream>
#include <iostream>
#include <string>

LogFileManager::LogFileManager() {}

LogFileManager::~LogFileManager() {
    if (outf.is_open()) {
        outf.close(); 
    }
    if (inpf.is_open()) {
        inpf.close();
    }
}

template <class sint, class sgf2n>
void LogFileManager::generate_log_title_file(int &id_log, Processor<sint, sgf2n>* processor) {
    title_inpf.open(LOG_TITLE_FILE_PATH);
    if (title_inpf.fail()) {
        system(("mkdir -p " + string(LOG_DIR)).c_str());
        title_outf.open(LOG_TITLE_FILE_PATH, ios::out);
        title_outf << "LOG_TITLE" << endl << id_log << endl;
        title_outf.close();
    } else {
        string ttmp;
        title_inpf >> ttmp >> id_log;
        id_log++;
        title_outf.open(LOG_TITLE_FILE_PATH, ios::out | ios::trunc);
        title_outf << "LOG_TITLE" << endl << id_log << endl;
        title_outf.close();
    }
    title_inpf.close();
}

template <class sint, class sgf2n>
void LogFileManager::generate_log_file(int &id_log, Processor<sint, sgf2n>* processor) {
    outf.open(LOG_ITEM_FILE_PATH(id_log), ios::out | ios::trunc);
    if (! outf.good()) {
        throw runtime_error(
            "^^^^^^^^^^^^^^^^^^^^Err in opening target file.^^^^^^^^^^^^^^^^^^^^");
    }
}

void LogFileManager::end_generate_log_file() {
    if (outf.is_open()) {
        outf.close();
    }
}

void LogFileManager::dump_time() {
    time_t rawtime;
    struct tm *ptminfo;
    time(&rawtime);
    ptminfo = localtime(&rawtime);
    dump_to_file("time\n", ptminfo -> tm_year + 1900, " ", ptminfo -> tm_mon + 1, " ");
    dump_to_file(ptminfo -> tm_mday, " ", ptminfo -> tm_hour, " ");
    dump_to_file(ptminfo -> tm_min, " ", ptminfo -> tm_sec, "\n");
}

template <class sint, class sgf2n>
void LogFileManager::dump_basic_info(int id_log, Processor<sint, sgf2n>* processor) {
    dump_to_file("id\n", id_log, "\n");
    dump_to_file("player_no\n", (processor -> P).my_num(), "\n");
    dump_to_file("nthreads\n", (processor -> machine).nthreads, "\n");
    dump_time();
}

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
        dump_processor_log(&PROCESSOR_LOGS[i]);
    }
}

template <class sint, class sgf2n>
void LogFileManager::dump_log(Log<sint, sgf2n>* log, Processor<sint, sgf2n> *processor) {
    int id_log = 0;
    generate_log_title_file(id_log, processor);
    generate_log_file(id_log, processor);
    dump_basic_info(id_log, processor);
    dump_pthread_func(log);
}

// Producer's func to consume source
template <class sint, class sgf2n>
void* LogFileManager::dump_pthread_func(Log<sint, sgf2n>* log) {
    dump_to_file("MachineLog\n");
    dump_machine_log(log);
    dump_to_file("ProcessorLogs\n");
    dump_to_file("Processors\n");
    dump_processor_logs(log);
    end_generate_log_file();
    // Any Other TODO?
    return nullptr;
}
