num1 = 0
num2 = 1

print(num1)
print(num2)

for i in range(20):
    newNum = num1 + num2
    print(newNum)
    num1 = num2
    num2 = newNum
    
    