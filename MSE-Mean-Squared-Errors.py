#https://www.mygreatlearning.com/blog/mean-square-error-explained/
#website where I found the mean square error

from termcolor import colored
def error(ArrA, ArrB, max):
    ArrC = []
    for i in range(max):
        ArrC.append(ArrA[i] - ArrB[i]) 
    return ArrC
def mse(ArrC, max):
    for i in range (max):
        ArrC[i] = ArrC[i] ** 2
    return ArrC

def mean(ArrC, max):
    sum = 0
    for i in range (max):
        sum += ArrC[i]
    mean = sum / max
    return mean
#delete this if you want, I made this because I was bored...
def misc(max):
    if max > 694206.66:
        print("Isn't a little bit too big?")
        print("Are you sure you want to continue?")
        choice = input(str())
        if (choice == 'y' or choice == 'Y'):
            hey = True
        else:
            hey = False
            quit()
        
#declaration
ArrA = []
ArrB = []
ArrC = []
print("\tThis program allow you to automatically find the", colored('MSE', 'blue'))
print(colored('\tRead more about MSE', 'green'))
print(colored('\thttps://www.mygreatlearning.com/blog/mean-square-error-explained/\n\n', 'blue'))
max = int(input("Enter the max for array: "))
misc(max)
temp = 0
i = -1
#it makes the value error go away
print("Enter the array A: ")
while True:
    try:
        temp = int(input())
        ArrA.append(temp)
        i += 1
        if (i == max - 1):
            break
    except ValueError:
        continue

print("Enter the array B you want to insert: ")
temp = 0
i = -1
#it makes the value error go away
while True:
    try:
        temp = int(input())
        ArrB.append(temp)
        i += 1
        if (i == max - 1):
            break
    except ValueError:
        continue

ArrC = error(ArrA, ArrB, max)
Mse = mse(ArrC, max) 
mean = mean(ArrC, max)
print("\t| The result is =", mean, '|')
