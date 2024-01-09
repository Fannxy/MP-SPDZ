// -----------------Bugs(Maybe)---------------
// 1.!!!!! MUST-TODO: check Memory leak, i.e. add `delete` for `new`.  
// 2.heck deep copy() or ptr copy to avoid messy in multi-threads.
// -----------------TODO Lists---------------
// 1.add pthread func for calling of dump_pthread_func in LogFileManager::dump_log()
// 2.Check Logic for BasicBlocks, or just add check_point(dump_log=True) at first of every BaicBlocks
// 3.Add conuter in online-threads's main loop, and call for Log::generate_log() && LogFileManager::dump_log() automatically
// (continue) via first of every basic_block
// 4.Add an onlineoption as a switch for the automatic dump_log function above
// 5. Check why there is a '8192' in MachineLog's Memory 
#ifndef _LOG_
#define _LOG_

#include "Tools/CheckVector.h"
#include "Processor/Processor.h"
#include "Processor/MachineLog.h"
#include "Processor/ProcessorLog.h"

using namespace std;    // in SPDZ many .h file using std as namespace, is it right?

template <class sint, class sgf2n>
class Log {

public:
    // Processor ptr
    Processor<sint, sgf2n> *processor;

    // Aims to generate Machine_Log.
    MachineLog<sint, sgf2n> *machine_log;

    // Aims to generate Processor_Logs.
    CheckVector<ProcessorLog<sint, sgf2n>> processor_logs;

    Log(Processor<sint, sgf2n> *processor);

    void generate_machine_log(Processor<sint, sgf2n> *processor);

    void generate_current_processor_log(Processor<sint, sgf2n> *processor);

    void generate_processor_logs();

    void generate_log();

    void read_log();

};
#endif