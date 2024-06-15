"""
Write a Python function called max_num()to find the maximum of three numbers.
Write a Python function called mult_list() to multiply all the numbers in a list.
Write a Python function called rev_string() to reverse a string.
Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
"""

def max_num(num1, num2, num3):
    return max([num1, num2, num3])

print(max_num(23, 54, 16))

def mult_list(nums):
    if len(nums) == 0:   
        return 0
    else:
        product = 1
        for num in nums:
            product *= num
            
        return product
    
numbers = [2, 3, 6]
print(mult_list(numbers))

def rev_string(str):
    return str[::-1]

print(rev_string('courtney'))

def num_within(num, begin_range, end_range):
    if (num >= begin_range and num <= end_range):
        return True
    else:
        return False
    
print(num_within(6, 3, 10))

def pascal(n):
    triangle = [[1],[1,1]]
    #base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        #fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            #create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):
                #first number is 1
                if i == 0:
                    row.append(1)
                #intermediate nunmbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                #last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        #print triangle
        for row in triangle:
            print(row)

pascal(7)