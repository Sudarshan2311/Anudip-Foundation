'''2. Write a lambda function that takes one argument and returns 'Positive' if the number is greater than 0, 
'Negative' if it's less than 0, and 'Zero' if it's O. 
Test it with different numbers'''

fun=lambda a: 'positive' if a>0 else('negative' if a<0 else 'zero') 
print(fun(2))
print(fun(0))
print(fun(-6))

