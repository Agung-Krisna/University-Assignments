#include <iostream> 
#include <chrono>
#define MAX_ARRAY 10000
int arr[MAX_ARRAY];
void swap(int *a, int *b) 
{ 
    int temporary = *a; 
    *a = *b; 
    *b = temporary; 
} 

void bubblesort(int max) 
{ 
    int i, j; 
    bool swapped; 
    for (i = 0; i < max-1; i++) 
    { 
        swapped = false; 
        for (j = 0; j < max-i-1; j++) 
        { 
            if (arr[j] > arr[j+1]) 
            { 
                swap(&arr[j], &arr[j+1]); 
                swapped = true; 
            } 
        } 


        if (swapped == false) //if there's no swap, then quit.
            break; 
    } 
    } 
    

void showArray(int size)  
{  
    int start;  
    for (start = 0; start < size; start++)  
    {
        if (start == size - 1)
        {
            printf("%d\n", arr[start]);
        }
        else
        {
        printf("%d, ", arr[start]);
        }
    }
}  

int main() 
{ 
    int max;
    int start = 0;
    int low = 0;
    printf ("Enter the amount of data to insert to the array\n");
    scanf ("%d", &max);

    printf ("Enter the data you want to insert\n");
    for (start = 0; start < max; start ++)
    {
        scanf ("%d", &arr[start]);
    }

    auto t_start = std::chrono::high_resolution_clock::now();

    bubblesort (max);
    printf("Sorted array:\n");
    showArray (max);
    
    auto t_stop = std::chrono::high_resolution_clock::now();


    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t_stop - t_start);

    printf("Bubble Sort Algorithm\n");
    printf("Time taken to sort the array: %d microseconds\n", duration.count());

    return 0;
} 
