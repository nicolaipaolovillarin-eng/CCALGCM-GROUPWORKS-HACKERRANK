#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;


int main() {
    stack<int> stack1;
    stack<int> stack2;
    
    int q;
    cin >> q;
    
    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        
        if (type == 1) {
            int x;
            cin >> x;
            stack1.push(x);
        }
        else if (type == 2) {
            while (stack2.empty()) {
                while (!stack1.empty()){
                stack2.push(stack1.top());
                stack1.pop();
                }
            }           
            
            stack2.pop();
        }
        else if (type == 3) {
            if (stack2.empty()){ 
            while (!stack1.empty()){
                stack2.push(stack1.top());
                stack1.pop();
            }
        }                        
            
            cout << stack2.top() << endl;       

            }
}      
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
