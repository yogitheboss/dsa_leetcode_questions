#include<iostream>
#include<stdio.h>

using namespace std;
#define max 5

int front =-1;
int rear=-1;
int queue[max];

void del_ele(){

    // no value exist
    if(front==-1 && rear==-1){
        cout<<"underflow"<<endl;
        return;
    }

    // only one value 
    if(front ==rear){
        front=-1;
        rear=-1;
    }

    // front reached last index
    else if(front==max-1){
        front=0;
    }

    else{
        front+=1;
    }
}


void traverse(){
    // if linear queue
    if(rear>=front){
    for(int i=front;i<=rear;i++){
        cout<<queue[i]<<endl;
    }
    }

    // circular
    else{

        // front to end
        for(int i=front;i<max;i++){
        cout<<queue[i]<<endl;
        }
        // 0 to rear
        for(int i=0;i<=rear;i++){
        cout<<queue[i]<<endl;

        }
    }
}
void insert(int val){
    // full packed
    if((rear+1)%max==front){
        cout<<"OverFlow ,can't enter value";
        return;
    }

    // no value
    else if(front==-1&&rear==-1){
        front=0;
        rear=0;
    }

    // rear reached last index
    else if(front!=0 && rear==max-1){
        rear=0;
    }
    // rear incrementing circularly
    else{
        rear=(rear+1)%max;
    }

    queue[rear]=val;
    
}


int main(){

    insert(2);
    insert(4);
    insert(5);
    del_ele();
    del_ele();    
    insert(2);
    insert(3);
    insert(4);
    insert(5);
    del_ele();
    insert(4);
    traverse();

}