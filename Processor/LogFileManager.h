#ifndef _FLOGFILEMANAGER_
#define _FLOGFILEMANAGER_

#include "Processor/Processor.h"
#include "Processor/Log.h"
#include "Processor/MachineLog.h"
#include "Processor/ProcessorLog.h"


#include <fstream>
#include <iostream>

using namespace std;

#define LOG_DIR "Logs-Player" + to_string(player_num)
#define LOG_TITLE_FILE_NAME  "Title.log"
#define LOG_TITLE_FILE_PATH  (string(LOG_DIR) + "/" + string(LOG_TITLE_FILE_NAME)).c_str()
#define LOG_ITEM_FILE_NAME   "CheckPoint" + to_string(log_id) + ".log"
#define LOG_ITEM_FILE_PATH   (string(LOG_DIR) + "/" + string(LOG_ITEM_FILE_NAME)).c_str()

#define MACHINE_LOG (log -> machine_log)
#define M2_LOG (MACHINE_LOG -> M2_log)
#define MP_LOG (MACHINE_LOG -> Mp_log)
#define MI_LOG (MACHINE_LOG -> Mi_log)
#define MS_LOG (memory_log.MS_log)
#define MC_LOG (memory_log.MC_log)
#define PROCESSOR_LOGS (log -> processor_logs)
#define STACKI_LOG (processor_log -> stacki_log)
#define CI_LOG (processor_log -> Ci_log)
#define C_LOG (subprocessor_log -> C_log)
#define S_LOG (subprocessor_log -> S_log)

class LogFileManager {
public:
    ofstream title_outf;
    ifstream title_inpf;
    ofstream outf;
    ifstream inpf;

    int log_id;
    int player_num;
    int player_nthreads;

    int worker_id;

    LogFileManager(int id);
    
    ~LogFileManager();

    // dump func with file opperations
    void generate_log_title_file();

    void generate_log_file();

    // directly dump_func (consumer's main_func is at bottom)
    void dump_to_file() {};

    template<typename T, typename... Args>
    void dump_to_file(const T& value, const Args&... args) {
        outf << value;
        dump_to_file(args...);
    }

    void open_log_file();

    void close_log_file();

    void dump_basic_info();

    void dump_time();

    template <class sint, class sgf2n>
    void dump_machine_log(Log<sint, sgf2n>* log);

    template <class sint, class sgf2n, class T>
    void dump_memory_log(MemoryLog<sint, sgf2n, T> memory_log);

    template <class sint, class sgf2n>
    void dump_stacki(ProcessorLog<sint, sgf2n>* processor_log);

    template <class sint, class sgf2n>
    void dump_Ci(ProcessorLog<sint, sgf2n>* processor_log);

    template <class sint, class sgf2n, class T>
    void dump_subprocessor(SubProcessorLog<sint, sgf2n, T>* subprocessor_log);

    template <class sint, class sgf2n>
    void dump_processor_log(ProcessorLog<sint, sgf2n>* processor_log);

    template <class sint, class sgf2n>
    void dump_processor_logs(Log<sint, sgf2n>* log);

    template <class sint, class sgf2n>
    void prepare_dump_log(Processor<sint, sgf2n> *processor);

    // consumer's main_func called by mutex from Program::dump_log
    template <class sint, class sgf2n>
    static void* dump_entry(void* arg);

    template <class sint, class sgf2n>
    void dump_thread(Log<sint, sgf2n>* log);
};

#endif