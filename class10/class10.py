# lambda function
data : list[int] = [1,2,3,4,5,6,7,8,9,10]
# first x is param
# after semi colon : second x is value stored in param 
data = list(map(lambda x:x**2 , data))
print(data)

# Multiple parameter function with double steric will ask to process argument with keys and its return type will be dictionary


from typing import Callable

# 1st function created with type casting
def deco1 (func: Callable[[int], None])->Callable[[int], None]:
    
    # 2nd function created within function
    def wrap1(num1:int)-> None:
    
        # this is function body of wrap1 under deco1 function
        print(f'This is wrap1 function print 1 and wrap1 num1 is {num1}')
       
        # this is the argument which will be passed through deco1 function
        func(num1)
       
        # this is function body of wrap1 under deco1 function       
        print(f'This is wrap1 function print after func() and wrap1 num1 is {num1}')
       
        # here you have returned wrap1 answer
    return wrap1

@deco1
def say_hello (num2: int)-> None:
    print(f'hi there say_hello func number is {num2}')

say_hello(100)