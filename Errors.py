
import sys
d = ['d', 0, 2,0,7]

for i in d:
    try:
        print("The entry is", i)
        a = 42/d(int)


    except ZeroDivisionError:
        print("Not Allowed")

    except TypeError:
        print("Unrecognized character to divide")

    finally:
        print("the result is printed")


#
# try:
#     x=6
#     y=0
#     print(x/y)
# except ZeroDivisionError:
#     print("Cannot divide by zero")


#
# try:
#     f=open("hi3.txt","r")
#     print(f.read())
# except IOError:
#     print("the mode of file is incorrect")
# finally:
#     f.close()
#

# try:
#     x=int(input("Enter a number: "))
#     if x>20:
#         raise ValueError(x)
# except ValueError:
#     print(x,"Out of range")
# else:
#     print(x,"Accepted")

