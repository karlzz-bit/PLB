#include "init.h"
#define MaxSize 10
typedef struct 
{
    char data[MaxSize];
    int top;
}SqStack;
void InitStack(SqStack &S);
bool StackEmpty(SqStack S);
bool Push(SqStack &S, char x);
bool Pop(SqStack &S, char &x);

bool bracketCheck(char str[],int length){
    SqStack S;
    InitStack(S);
    for(int i=0;i<length;i++){
        if(str[i]=='('||str[i]=='['||str[i]=='{'){
            Push(S,str[i]);
        }else{
            if(StackEmpty(S)){
                return false;
            }
            char topElem;
            Pop(S,topElem);
            if(str[i]==')'&&topElem!='('){
                return false;
            }
            if(str[i]==']'&&topElem!='['){
                return false;
            }
            if(str[i]=='}'&&topElem!='{'){
                return false;
            }
        }
    }
    return StackEmpty(S);
}
