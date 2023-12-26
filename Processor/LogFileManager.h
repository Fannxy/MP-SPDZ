#ifndef _FLOGFILEMANAGER_
#define _FLOGFILEMANAGER_

#include "Processor/Processor.h"

#include <fstream>
#include <iostream>

using namespace std;

#define LOG_DIR "Logs-Player" + to_string(((this -> processor) -> P).my_num())
#define LOG_TITLE_FILE_NAME  "Title.log"
#define LOG_TITLE_FILE_PATH  (string(LOG_DIR) + "/" + string(LOG_TITLE_FILE_NAME)).c_str()
#define LOG_ITEM_FILE_NAME(x)   "CheckPoint" + to_string(x) + ".log"
#define LOG_ITEM_FILE_PATH(x)   (string(LOG_DIR) + "/" + string(LOG_ITEM_FILE_NAME(x))).c_str()
#define LOGOUT(...) (this -> log_file_manager) -> dump_to_file(__VA_ARGS__)

template <class sint, class sgf2n>
class LogFileManager {
private:
    static LogFileManager* instance;
    ofstream title_outf;
    ifstream title_inpf;
    ofstream outf;
    ifstream inpf;
    Processor<sint, sgf2n> *processor;

    LogFileManager(Processor<sint, sgf2n> *processor);

    LogFileManager(const LogFileManager&) = delete;
    LogFileManager& operator=(const LogFileManager&) = delete;

public:
    static LogFileManager& getInstance(Processor<sint, sgf2n> *processor) {
        static LogFileManager instance(processor);
        return instance;
    }
    
    ~LogFileManager();

    void generate_log_title_file(int &id_log);

    void generate_log_file(int &id_log);

    void dump_to_file() {};

    template<typename T, typename... Args>
    void dump_to_file(const T& value, const Args&... args) {
        outf << value;
        dump_to_file(args...);
    }

    void end_generate_log_file();
};

#endif