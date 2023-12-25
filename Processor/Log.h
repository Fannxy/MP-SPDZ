#ifndef _LOG_
#define _LOG_

#include "Processor/MachineLog.h"
#include "Processor/ProcessorLog.h"
#include "Tools/CheckVector.h"
#include "Processor/Machine.h"
#include "Processor/Processor.h"

using namespace std;    // in SPDZ many .h file using std as namespace, is it right?


template <class sint, class sgf2n>
class Log {

public:
    // id
    int id_log;

    // target file && source file
    ofstream outf;
    ifstream inf;

    // Processor ptr
    Processor<sint, sgf2n> *processor;

    // Aims to generate Machine_Log.
    MachineLog<sint, sgf2n> *machine_log;

    // Aims to generate Processor_Logs.
    CheckVector<ProcessorLog<sint, sgf2n>*> processor_logs;

    Log(Processor<sint, sgf2n> *processor);

    struct tm* get_time();

    void dump_machine_log(Machine<sint, sgf2n> *machine);

    void dump_current_processor_log(Processor<sint, sgf2n> *processor);

    void dump_processor_logs();

    void dump_log();

    void dump_log_title(int &id_Log);

    void dump_log_file(int id_Log);

    void read_log();

};
#endif