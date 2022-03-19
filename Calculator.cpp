#include <iostream>

int check()
{
    bool done;
    int choice;
    while (done != true)
    {
    printf("Kalkulasi apa yang anda inginkan?\n");
    printf("1. pertambahan\n");
    printf("2. pengurangan\n");
    printf("3. perkalian\n");
    printf("4. pembagian\n");
    printf("5. modulus\n");
    scanf("%d", &choice);
    if (choice >= 1 && choice <= 5)
    {
        done = true;
    }
    else
    {
        printf("Unexpected choice, trying again\n");
        done = false;
    }
    }
    return choice;
}

float addition(float a, float b)
{
    return a + b;
}
float subtraction(float a, float b)
{
    return a - b;
}
float multiplication(float a, float b)
{
    return a * b;
}
float division (float a, float b)
{
    return a / b;
}
int modulus (int a, int b)
{
    return a % b;
}
int main()
{
    int choice;
    choice = check();
    float result;
    float a, b;
    printf("Masukkan sebuah angka untuk dikalkulasikan:\n");
    scanf("%f", &a);
    
    printf("Masukkan sebuah angka untuk dikalkulasikan:\n");
    scanf("%f", &b);
    switch(choice)
    {
        case 1:
            result = addition(a, b);
            break;
        case 2:
            result = subtraction(a, b);
            break;
        case 3:
            result = multiplication(a, b);
            break;
        case 4:
            if (b == 0)
            {
                printf("Unexpected ZeroDivisionError, please try again\n");
                return EXIT_FAILURE;
            }
            result = division(a, b);
            break;
        case 5: 
            result = modulus(int(a), int(b));
            break;
        default:
            printf("Error occured, please try again\n");
    }
    if (result - int(result) != 0)
    {
        printf("the result of the calculation: %f\n", result);
    }
    else
    {
        printf("the result of the calculation: %.0f\n", result);
    }
}
