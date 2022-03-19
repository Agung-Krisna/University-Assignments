#include <iostream>
using std::string;

int stack[10];
int n = 10;
int top = -1;

void push(int value) {
    if(top >= n-1)
        printf ("Stack Overflow, too much data entered\n");
    else {
        top++;
        stack[top] = value;
   }
}
void pop() {
   if(top <= -1)
        printf ("Stack Underflow, no data was found on the stack\n");
   else {
        printf ("Element popped! The element that was popped %d", stack[top]);
        top --;
   }
}
void peek() {
   if(top>= 0) {
      printf ("Peeking the stack...\n");
      for(int start = top; start >= 0; start--)
         printf ("%d\n", stack[start]);
      std::cout<<std::endl;
   } else
      printf ("Stack is empty\n");
}
int main() {
    int choice;
    int value;
    printf ("Enter what you want to do:\n");
    printf ("(1) Push elements into the stack\n");
    printf ("(2) Pop elements from the stack\n");
    printf ("(3) Peek the elements from the stack\n");
    printf ("(4) Exit the program\n");
    scanf ("%d", &choice);
        while (choice != 4){
            if (choice == 1){
                printf ("Enter the element that you want to push into the stack:\n");
                scanf ("%d", &value);
                push(value);
                continue;
                }
            else if (choice == 2){
                printf ("Popping the element...\n");
                pop();
                continue;
                }
            else if (choice == 3){
                printf ("Peeking the elements...\n");
                peek();
                continue;
                }
            else {
                printf ("Entered number was not present on the list, quitting\n");
                return EXIT_FAILURE;
                }
        }
        printf ("Program is terminated\n");
        return EXIT_SUCCESS;
}
