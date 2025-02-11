my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

# Your code here

Total = 0
Total_Items = len(my_list)

for num in my_list:
    Total += num

average = Total / Total_Items 
print(average)

