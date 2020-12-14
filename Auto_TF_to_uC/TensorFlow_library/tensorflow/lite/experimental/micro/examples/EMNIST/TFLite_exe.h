#include "./EMNIST_model_data.h"
#include "./../../kernels/all_ops_resolver.h"
#include "./../../micro_error_reporter.h"
#include "./../../micro_interpreter.h"
#include "./../../../../schema/schema_generated.h"
#include "./../../../../version.h"

#include <cstdio>


void setup(); 
void model_execute(float *, char *, float *, char *, float *, char *, float *);
