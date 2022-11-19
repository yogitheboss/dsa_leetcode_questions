#include<bits/stdc++.h>
using namespace std;
void showq(queue<int> gq)
{
    queue<int> g = gq;
    while (!g.empty()) {
        cout << '\t' << g.front();
        g.pop();
    }
    cout << '\n';
}
queue<int> modifyQueue(queue<int> q, int k) {
//    initialising an empty stack
   stack<int> s;
   int temp=k;
   while(k>0){
    // adding first k elements in the stack and removing from queue
   k--;
   s.push(q.front());
   q.pop();
   }
   while(!s.empty()){
    // pushing the value from stack to queue and also emptying the stack
       q.push(s.top());
       s.pop();
   }
//    now we just have to arrange the queue, now put the front elements of queue i.e. non modified elements to the back on the queue

// total non modified values= total-k
   for(int i=0;i<q.size()-temp;i++){
       q.push(q.front());
       q.pop();
   }
   return q;
   
}
int main(){
    queue<int> q;
    q.push(4);
    q.push(5);
    q.push(7);
    q.push(9);
    q.push(10);
    int k=3;
    showq(q);
    cout<<endl;
    q=modifyQueue(q,k);
    showq(q);

}