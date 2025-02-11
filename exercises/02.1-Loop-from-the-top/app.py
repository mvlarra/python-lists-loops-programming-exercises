my_sample_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

# Modify the loop below to print from end to start

# print("\n*** ANALITICAL STEPS: ")
# print('Items:   ' + format(len(my_sample_list)))
# print('Lista:   ' + format(my_sample_list))
# print("Reverse: " + format(my_sample_list.reverse()))


# print("\n*** SOLUTION:")
for i in range(len(my_sample_list)-1,-1,-1):
    print(my_sample_list[i])

# # for i in range(13,-1,-1):
# #     print(my_sample_list[i])

# ############## TESTING

# print("\n*** TESTING:")

# # Range Function include the Start (the first index), 
# # but exclude the Stop (The last index) 
# my_test_list_1a10 = range(0,11)
# print("Beginning to End: " + format(list(my_test_list_1a10)))

# my_test_list_10a1 = range(10,0-1,-1)
# print("End to Beginning: " + format(list(my_test_list_10a1)))

# # The 3th parameter in the range funtion is called "step". 
# # It says how to increase / decress the next value in the range
# my_test_list_2 = range(1,11,2)
# print("Increment by 2: " + format(list(my_test_list_2)))







