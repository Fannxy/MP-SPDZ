#include <sys/stat.h>
#include <errno.h>
#include <cstdlib> 

#include "Processor/LogFileManager.hpp"

LogFileManager::LogFileManager(int worker_id): worker_id(worker_id) {}

LogFileManager::~LogFileManager() {
    if (outf.is_open()) {
        outf.close(); 
    }
    if (inpf.is_open()) {
        inpf.close();
    }
}

void LogFileManager::generate_log_title_file() {
    if (!directoryExists(LOG_DIR)) {
        int ret = mkdir(LOG_DIR.c_str(), 0777);
        if (ret) {
            cout << "Try mkdir, path: " << ("mkdir -p " + string(LOG_DIR)).c_str() << endl;
            cout << "ret code " << ret << endl;
            throw runtime_error(
                "^^^^^^^^^^^^^^^^^^^^Err in mkdir command.^^^^^^^^^^^^^^^^^^^^");
        }
        title_outf.open(LOG_TITLE_FILE_PATH, ios::out);
        log_id = 0;
    } else {
        title_inpf.open(LOG_TITLE_FILE_PATH);
        string ttmp;
        title_inpf >> ttmp >> log_id;
        title_inpf.close();
        log_id++;
        title_outf.open(LOG_TITLE_FILE_PATH, ios::out | ios::trunc);
    }
    title_outf << "LOG_TITLE" << endl << log_id << endl;
    title_outf.close();
}

void LogFileManager::generate_log_file() {
    outf.open(LOG_ITEM_FILE_PATH, ios::out | ios::trunc);
    if (! outf.good()) {
        throw runtime_error(
            "^^^^^^^^^^^^^^^^^^^^Err in opening target file.^^^^^^^^^^^^^^^^^^^^");
    }
    outf.close();
}

bool LogFileManager::directoryExists(const std::string& directory) {
    struct stat info;
    return stat(directory.c_str(), &info) == 0 && S_ISDIR(info.st_mode);
}

void LogFileManager::open_log_file() {
    outf.open(LOG_ITEM_FILE_PATH, ios::out | ios::app);
    if (! outf.good()) {
        throw runtime_error(
            "^^^^^^^^^^^^^^^^^^^^Err in opening target file.^^^^^^^^^^^^^^^^^^^^");
    }
}

void LogFileManager::close_log_file() {
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

void LogFileManager::dump_basic_info() {
    dump_to_file("id\n", log_id, "\n");
    dump_to_file("player_no\n", player_num, "\n");
    dump_to_file("nthreads\n", player_nthreads, "\n");
    dump_time();
}