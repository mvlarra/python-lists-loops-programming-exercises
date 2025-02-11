the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def YesOrNo(num):
        if num == 1: 
            return "Wiki"
        else:
            return "Woko"
    
NL = list(map(YesOrNo, the_bools))
print(NL)


#OTRA SOLUCION:

# new_list = list(map(lambda x: 'wiki' if x == 1 else 'woko', the_bools))

# print(new_list)
