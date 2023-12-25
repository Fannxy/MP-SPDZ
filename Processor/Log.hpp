#include "Log.h"
#include "Processor/Machine.h"
#include "Processor/Processor.h"
#include <ctime>
#include <fstream>
#include <iostream>
#include <cstring>
#include <cstdlib>


#define LOG_DIR "Logs"
#define LOG_TITLE_FILE_NAME  "Title.log"
#define LOG_TITLE_FILE_PATH  (string(LOG_DIR) + "/" + string(LOG_TITLE_FILE_NAME)).c_str()
#define LOG_ITEM_FILE_NAME(x)   "Item" + to_string(x) + ".log"
#define LOG_ITEM_FILE_PATH(x)   (string(LOG_DIR) + "/" + string(LOG_ITEM_FILE_NAME(x))).c_str()


template <class sint, class sgf2n>
Log<sint, sgf2n>::Log(Processor<sint, sgf2n> *processor) {
    this -> processor = processor;
}

template <class sint, class sgf2n>
struct tm* Log<sint, sgf2n>::get_time() {
    time_t rawtime;
    struct tm *ptminfo;
    time(&rawtime);
    ptminfo = localtime(&rawtime);
    return ptminfo;
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_machine_log(Machine<sint, sgf2n> *machine) {
    machine_log = new MachineLog(machine);
    this -> machine_log = machine_log;
    (this -> machine_log) -> dump_machinelog(outf);
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_current_processor_log(Processor<sint, sgf2n> *processor) {
    this -> processor_logs.push_back(&(ProcessorLog(processor)));
    (this -> processor_logs)[processor_logs.size() - 1] -> dump_processorlog();
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_processor_logs() {
    throw runtime_error(
            "^^^^^^^^^^^^^^^^^^^^No implemented for multi-threads circumstances^^^^^^^^^^^^^^^^^^^^");
    return;
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_log_title(int &id_Log) {
    ifstream inpf;
    inpf.open(LOG_TITLE_FILE_PATH);
    ofstream outf;
    if (inpf.fail()) {
        system(("mkdir " + string(LOG_DIR)).c_str());
        outf.open(LOG_TITLE_FILE_PATH, ios::out);
        outf << "LOG_TITLE" << endl << id_Log << endl;
        outf.close();
    } else {
        string ttmp;
        inpf >> ttmp >> id_Log;
        id_Log++;
        outf.open(LOG_TITLE_FILE_PATH, ios::out | ios::trunc);
        outf << "LOG_TITLE" << endl << id_Log << endl;
        outf.close();
    }
    inpf.close();
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_log() {
    cout << "11111111111111111111111" << ((this -> processor) -> P).my_num() << endl;
    int id_Log = 0;
    Log<sint, sgf2n>::dump_log_title(id_Log);
    dump_log_file(id_Log);
    outf << "id " << id_Log << " " << ((this -> processor) -> P).my_num() << endl;
    Log<sint, sgf2n>::get_time();
    struct tm *ptminfo = get_time();;
    outf << ptminfo -> tm_year + 1900 << " " << ptminfo -> tm_mon + 1;
    outf  << " " << ptminfo -> tm_mday << " " << ptminfo -> tm_hour;
    outf << " " << ptminfo -> tm_min <<  " " << ptminfo -> tm_sec << endl;
    // dump_machine_log(&((this -> processor) ->machine));
    // outf << "nthreads" << endl;
    // outf << ((this -> processor)->machine).nthreads << endl;
    // if (((this -> processor)->machine).nthreads == 1) {
    //    dump_current_processor_log((this -> processor));
    // } else {
    //     dump_processor_logs();
    // }
    // otherTODO?
    outf.close (); // ChatGPT says only need to close file once in final.
    return;
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::dump_log_file(int id_Log) {
    (this->outf).open(LOG_ITEM_FILE_PATH(id_Log), ios::out | ios::trunc);
    if (! (this->outf).good()) {
        throw runtime_error(
            "^^^^^^^^^^^^^^^^^^^^Err in opening target file.^^^^^^^^^^^^^^^^^^^^");
    }
}

template <class sint, class sgf2n>
void Log<sint, sgf2n>::read_log() {
    throw runtime_error(
        "^^^^^^^^^^^^^^^^^^^^No implemented for reloading^^^^^^^^^^^^^^^^^^^^");
}