nums = [22, 3, 4, 55, 6, 77, 8, 99, 10]
result = [num for num in nums if(num %3 ==0 and num %9 ==0)]
print(result) # output: [99]

nums = [22, 3, 4, 55, 6, 77, 8, 99, 10]
result2 = [num for num in nums if(num%2==0 and num%3==0)]
print(result2) # output: [6]

print("Some Changes")
print("some Extra Changes")
