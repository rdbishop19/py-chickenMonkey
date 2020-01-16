'''
Write a program that prints the numbers from 1 to 100. 
You can use Python's range() to quickly make a list of numbers.

For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
For the multiples of seven (7, 14, 21, etc.) print "Monkey".
For numbers which are multiples of both five and seven print "ChickenMonkey".
To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.
'''

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i,'chickenMonkey')
    elif i % 5 == 0:
        print(i, 'chicken')
    elif i % 7 == 0:
        print(i, 'monkey')
    else:
        print(i)