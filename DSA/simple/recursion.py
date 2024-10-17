print(0)
print(1)

count = 2

def fibonacci(num1,num2):
    global count
    if count <= 20:
        newNum = num1 + num2
        print(newNum)
        num2 = num1
        num1 = newNum
        count +=1
        fibonacci(num1,num2)
    else:
        return
    
    
num1 = 0
num2 = 1
fibonacci(num1,num2)
