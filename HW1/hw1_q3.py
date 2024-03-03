# Write a program that iterates from 1 to 20, printing each number and whether 
# it's odd or even.

def main():
    for i in range (1, 21):
        if(i%2==0):
            print(str(i) + " is even")
        else:
            print(str(i) + " is odd")
main()