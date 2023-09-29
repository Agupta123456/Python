b = int(input("Enter the integer number: "))  
  
revs_number = 0  
  
while (b > 0):  
    remainder = b % 10  
    revs_number = (revs_number * 10) + remainder  
    b = b // 10  
  
print("The reverse of b is :",revs_number)
