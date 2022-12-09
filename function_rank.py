import time
import random

# list = [1,3,5,4,6,2,7,0,9,8,11,19,13,14,16,28,29,34,33,22]

list = []
for i in range(1010):
    list.append(random.randint(0, 1000000))

sorted_list = []

# WAY 1
# lay 1 so va index cua no
# check voi cac so co index truoc do de xac dinh vi tri cua no trong array
# sau do them no vao trong mang tai vi tri do

# 1 mang can sorting
# 1 mang duoc sorted dan

def checking_element(idx,val):
    global sorted_list
    if idx < 0:
        temp_list_1 = [val]
        sorted_list = temp_list_1 + sorted_list
        return sorted_list
    if idx == 0 and len(sorted_list) == 0:
        sorted_list.append(list[idx])
        return sorted_list
    else:
        if sorted_list[idx-1] <= val:
            temp_list_1 = sorted_list[:idx]
            temp_list_1.append(val)
            try:
                temp_list_2 = sorted_list[idx:]
                sorted_list = temp_list_1 + temp_list_2
            except:
                sorted_list = temp_list_1
            return sorted_list
        else:
            return checking_element(idx-1, val)
        
# start = time.time()
# for i in range(len(list)):
#     sorted_list = checking_element(i, list[i])
# end = time.time()
# print(sorted_list) 

# line = f'Whole process takes {end - start}'
# print(line)



# WAY 2

def rank_list(list):
    global sorted_list
    if len(list) == 1:
        return list + sorted_list
    else:
        max = list[0]
        max_idx = 0
        i = 1
        for i in range(len(list)):
            if max < list[i]:
                max = list[i]
                max_idx = i
        sorted_list = [max] + sorted_list
        temp_list_1 = list[:max_idx]
        if max_idx == len(list) - 1:
            list = temp_list_1
        else:
            temp_list_2 = list[max_idx+1:]
            list = temp_list_1 + temp_list_2
        return rank_list(list)

# start = time.time()
# sorted_list = rank_list(list)
# end = time.time()
# print(sorted_list)

# line = f'Whole process takes {end - start}'
# print(line)


# WAY 3 BUILT-IN FUNCTION

# start = time.time()
# list.sort()
# end = time.time()
# print(list)
# line = f'Whole process takes {end - start}'
# print(line)
