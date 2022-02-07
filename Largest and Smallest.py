#Largest, Smallest,2nd Largest, 2nd Smallest

list = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)
print("Largest element in the list is :", max(list))
print("Smallest element in the list is :", min(list))
list.sort()
print("Second largest element is:", list[-2])
print("Second smallest element is:", list[1])


#Swapping

# x = int(input("Enter the num: "))
# y = int(input("Enter the num: "))
#
# print("Before swapping: ")
# print("Value of x : ", x, " and y : ", y)
# x, y = y, x
# print("After swapping: ")
# print("Value of x : ", x, " and y : ", y)





