#include <stdio.h>
#include <stdlib.h>

int main(){
    int max;
    int array[100];
    int start = 0;
    int value = 0;

    printf ("Put maximum amount of array here:\n");
    scanf ("%d", &max);

    printf ("Enter %d amount of data:\n", max);
    for (start = 0; start < max; start ++){
        scanf ("%d", &array[start]);
    }
    for (start = 0; start < max; start++){
        if (array[start] > array[value]){ //if the array[start] is bigger than the array[value], then save the value. 
            value = start;
        }
    }
    printf ("Max value is: %d", array[value]);
    return 0;
}
