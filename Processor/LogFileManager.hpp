#include "Processor/LogFileManager.h"

#include <fstream>
#include <iostream>
#include <string>

template <class sint, class sgf2n>
LogFileManager<sint, sgf2n>::LogFileManager(Processor<sint, sgf2n> *processor) {
    this->processor = processor;
}

template <class sint, class sgf2n>
LogFileManager<sint, sgf2n>::~LogFileManager() {
    if (outf.is_open()) {
        outf.close(); 
    }
    if (inpf.is_open()) {
        inpf.close();
    }
}

template <class sint, class sgf2n>
void LogFileManager<sint, sgf2n>::generate_log_title_file(int &id_log) {
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
void LogFileManager<sint, sgf2n>::generate_log_file(int &id_log) {
    outf.open(LOG_ITEM_FILE_PATH(id_log), ios::out | ios::trunc);
    if (! outf.good()) {
        throw runtime_error(
            "^^^^^^^^^^^^^^^^^^^^Err in opening target file.^^^^^^^^^^^^^^^^^^^^");
    }
}

template <class sint, class sgf2n>
void LogFileManager<sint, sgf2n>::end_generate_log_file() {
    if (outf.is_open()) {
        outf.close();
    }
}




