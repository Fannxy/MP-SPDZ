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
    CheckVector<ProcessorLog<sint, sgf2n>*> processor_logs;

    Log(Processor<sint, sgf2n> *processor);

    ~Log();
    
    void generate_machine_log(Processor<sint, sgf2n> *processor);

    void generate_current_processor_log(Processor<sint, sgf2n> *processor);

    void generate_processor_logs();

    void generate_log();

    void read_log();

};
#endif