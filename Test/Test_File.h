#include "Lambda.h"

typedef struct Test_Struct
{
    int Value;
} Test_Struct;

void Test_Fn()
{
    char* (*fn)(int, Test_Struct*) = Lambda(char*, (int value, Test_Struct* data))();
}