#ifndef _FLOGFILEMANAGER_
#define _FLOGFILEMANAGER_

#include "Processor/Processor.h"
#include "Processor/Log.h"
#include "Processor/MachineLog.h"
#include "Processor/ProcessorLog.h"


#include <fstream>
#include <iostream>

using namespace std;

#define LOG_DIR "Logs-Player" + to_string(((this -> processor) -> P).my_num())
#define LOG_TITLE_FILE_NAME  "Title.log"
#define LOG_TITLE_FILE_PATH  (string(LOG_DIR) + "/" + string(LOG_TITLE_FILE_NAME)).c_str()
#define LOG_ITEM_FILE_NAME(x)   "CheckPoint" + to_string(x) + ".log"
#define LOG_ITEM_FILE_PATH(x)   (string(LOG_DIR) + "/" + string(LOG_ITEM_FILE_NAME(x))).c_str()

#define MACHINE_LOG ((this -> log) -> machine_log)
#define M2_LOG (MACHINE_LOG -> M2_log)
#define MP_LOG (MACHINE_LOG -> Mp_log)
#define MI_LOG (MACHINE_LOG -> Mi_log)
#define MS_LOG (memory_log.MS_log)
#define MC_LOG (memory_log.MC_log)
#define PROCESSOR_LOGS ((this -> log) -> processor_logs)
#define STACKI_LOG (processor_log -> stacki_log)
#define CI_LOG (processor_log -> Ci_log)
#define C_LOG (subprocessor_log -> C_log)
#define S_LOG (subprocessor_log -> S_log)

template <class sint, class sgf2n>
class LogFileManager {
public:
    static LogFileManager* instance;
    ofstream title_outf;
    ifstream title_inpf;
    ofstream outf;
    ifstream inpf;
    Processor<sint, sgf2n> *processor;
    Log<sint, sgf2n> *log;

    LogFileManager(Processor<sint, sgf2n> *processor, Log<sint, sgf2n> *log);
    
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

    void dump_basic_info(int id_log);

    void dump_time();

    void dump_machine_log();

    template <class T>
    void dump_memory_log(MemoryLog<sint, sgf2n, T> memory_log);

    void dump_stacki(ProcessorLog<sint, sgf2n>* processor_log);

    void dump_Ci(ProcessorLog<sint, sgf2n>* processor_log);

    template <class T>
    void dump_subprocessor(SubProcessorLog<sint, sgf2n, T>* subprocessor_log);

    void dump_processor_log(ProcessorLog<sint, sgf2n>* processor_log);

    void dump_processor_logs();

    void dump_pthread_func();

    void dump_log();
};

#endif