# File: chaos.py
# Created 12/11/18 by Macauley Tosi
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should i print? "))
    for i in range(n):
        x = 3.9 * x - 3.9 * x * x 
        print(x)
main()
