#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
    struct node* next;
    char data;
}NODE;

typedef struct{
    NODE* Top;
    int count;

}STACK;

STACK* createStack(){
    STACK* stack;

    stack=(STACK*)malloc(sizeof(STACK));

    if(stack){
        stack->Top=NULL;
        stack->count=0;
    }
    printf("Stack olusturuldu\n\n");
    return stack;

}

void push(STACK* pstack, char data){

    NODE* pNew= (NODE*)malloc(sizeof(NODE)); // I can put this node into heap with this code
    pNew->data=data;
    pNew->next=NULL;

    if(pstack->Top==NULL){ //While stack is empty
        pstack->Top=pNew;
        pstack->count++;
    }
    else{ // while the stack has more than one node
        pNew->next=pstack->Top;
        pstack->Top=pNew;
        pstack->count++;
    }

}

char pop(STACK* pstack){
    NODE* popped;
    char dataToPopped;

    if(pstack->count>1){
        popped=pstack->Top;
        dataToPopped=pstack->Top->data;
        pstack->Top=pstack->Top->next;
        free(popped);
        pstack->count--;
    }
    else if(pstack->count==1){

        popped=pstack->Top;
        dataToPopped=pstack->Top->data;
        pstack->Top=NULL;
        pstack->count--;
        free(popped);
    }
    return dataToPopped;
}

bool isValid(char * s){
    STACK* stack= createStack();
    bool isPushedAny=false;
    if(strlen(s)%2==0){
    for(int i=0; i<strlen(s); i++){
        if(s[i]=='{' || s[i]=='(' || s[i]=='['){
            push(stack,s[i]);
            isPushedAny=true;
        }
        else{
            if(stack->count==0){
                return false;
            }
            
            char dataToCompare;
            dataToCompare=pop(stack);
            if(dataToCompare=='{' && s[i]!='}' || dataToCompare=='(' && s[i]!=')' || dataToCompare=='[' && s[i]!=']'){
                return false;
            }
        }
    }
        
    }
    else{
        return false;
    }
    if(stack->count==0 && isPushedAny==true){
         return true;
    }
    
    return false;
    
}
