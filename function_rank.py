import time

list = [1,3,5,4,6,2,7,0,9,8]

sorted_list = []

# WAY 1
# lay 1 so va index cua no
# check voi cac so co index truoc do de xac dinh vi tri cua no trong array
# sau do them no vao trong mang tai vi tri do

# 1 mang can sorting
# 1 mang duoc sorted dan
# start = time.time()

# def checking_element(idx,val):
#     global sorted_list
#     if idx < 0:
#         temp_list_1 = [val]
#         sorted_list = temp_list_1 + sorted_list
#         return sorted_list
#     if idx == 0 and len(sorted_list) == 0:
#         print("Test1")
#         sorted_list.append(list[idx])
#         return sorted_list
#     else:
#         print("Test2")
#         if sorted_list[idx-1] <= val:
#             print('1-', sorted_list)
#             temp_list_1 = sorted_list[:idx]
#             print('temp 1', temp_list_1)
#             temp_list_1.append(val)
#             print('temp 2', temp_list_1)
#             try:
#                 temp_list_2 = sorted_list[idx:]
#                 sorted_list = temp_list_1 + temp_list_2
#             except:
#                 sorted_list = temp_list_1
#             print('2-', sorted_list)
#             return sorted_list
#         else:
#             return checking_element(idx-1, val)
        
    
# for i in range(len(list)):
#     print(i)
#     sorted_list = checking_element(i, list[i])
#     print(sorted_list)
    
# end = time.time()
# line = f'Whole process takes {end - start}'
# print(line)



#WAY 2
start = time.time()

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

sorted_list = rank_list(list)
print(sorted_list)

end = time.time()
line = f'Whole process takes {end - start}'
print(line)