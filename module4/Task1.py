#Factorial using recursion

def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)
n=int(input('Enter a number: '))
print('Factorial of ',n,'is:',factorial(n))

#Factorial using loop

def factorial_loop(n):
    if n<2:
        return 1
    else:
        ans=1
        for i in range(1,n+1):
            ans=ans*i
    return ans
m=int(input('Enter a number: '))
print('Factorial of ',m,'is:',factorial_loop(m))




