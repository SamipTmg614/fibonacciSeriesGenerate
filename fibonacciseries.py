
def fibonacci(x):
    if x<=0:
        print('invalid input number, ht enumber must be positive integer!')
        return None
    a=0 
    b=1 
    print(a)
    print(b)  
    for i in range(2,x):
            c=a+b
            a=b
            b=c
            if c<=50:           
                print(c)

def fibonacci_series(num):

    if not isinstance(num,int):
        print('invalid input type')
        return None
    if num <=0:
        print('invalid input')
        return None
    
    if num==1:
        return[0]
        
    
    fibonacciseries =[0,1]

    for i in range(num - 2):
        next_item = fibonacciseries[-1] + fibonacciseries[-2]
        fibonacciseries.append(next_item)

    return fibonacciseries

