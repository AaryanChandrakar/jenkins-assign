nums = [22, 3, 4, 55, 6, 77, 8, 99, 10]
result = [num for num in nums if(num %3 ==0 and num %9 ==0)]
print(result) # output: [99]
