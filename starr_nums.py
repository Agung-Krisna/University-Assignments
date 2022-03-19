#!/usr/bin/python3
#iteratively:
def stars(nums):
    if nums < 0:
        return
        exit()
    else:
        for i in range (nums + 1):
            for j in range (i):
                print("*", end = "")
            if (i == 0 or i == nums + 1):
                print(end = "")
            else:
                print(end = "\n")
def numbers(nums):
    if nums < 0:
        return
        exit()
    else:
        start = 1
        for i in range (nums):
            for j in range (i + 1):
                print(start, end = " ")
                start += 1
            print(end = "\n")
