#include <stdio.h>
#include <stdlib.h>

//I really don't want to use pointers because we haven't discussed about that yet, so, I'll try my best not to use them.
int main(){
    int Array[] = {12, 5, 7, 8, 2, 4, 10, 9, 6, 11, 1, 3}; //array size = 12
    int min;
    int start = 0;
    int swap;
    int start_inner;
    int size = sizeof(Array) / sizeof(int);
    
    printf ("Unsorted Array:");
    for (start = 0; start < size; start ++){
        printf ("[%d] ", Array[start]);
    }
    //Selection Sort Algorithm
    for (start = 0; start < (size - 1); start ++){//moving the array elements, starting from 0, until the last element - 2;
        min = start;//initiation of the min value
        for (start_inner = (start + 1); start_inner < size; start_inner ++){//checking the elements, starting from the first position
            if (Array[start_inner] < Array[min]){//checking whether the elements that are in the start_inner variable is more than the min variable
                min = start_inner;//changing the min elements into the start_inner
            }
        }
        if (min != start){//swapping algorithm, showed during the third lesson
            swap = Array[start];
            Array[start] = Array[min];
            Array[min] = swap;
        }
    }
    printf ("\nSorted Array is: \n");
    for (start = 0; start < size; start ++){
        printf ("%d", Array[start]);
        printf ("\n");
    }
}


//Quite a nice challenge...

//Will be posted after 3.50 PM Standard Singapore Time (GMT+8) in my GitHub.
//https://github.com/Agung-Krisna
