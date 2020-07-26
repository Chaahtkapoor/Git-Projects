n= int(input("Please Enter any Number: "))
sum = 0

for value in range(1, n + 1):
    sum = sum + value

average = sum / n
print ("average of", n, "number is", average)
#%%


num= int(input("Please Enter any Number: "))

factorial = 1
if num < 0:
    print("sorry, factorial does not exist")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num +1):
        factorial = factorial*i
    print("the factorial of", num, " is", factorial) 
 #%%
num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")
#%%
n= int(input("Enter your number"))
sum = 0
for i in range (1, n+1):
    sum = sum +(1/i)
print ("The sum of series is", round(sum,2))    
#%%
rows= int (input("Enter your number"))
for i in range (1,rows+1):
    for j in range (1, 1+i):
        print (j, end='')
    print("")    
