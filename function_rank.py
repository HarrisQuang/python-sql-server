# lay 1 so va index cua no
# check voi cac so co index truoc do de xac dinh vi tri cua no trong array
# sau do them no vao trong mang tai vi tri do

# 1 mang can sorting
# 1 mang duoc sorted dan

list = [1,3,5,4,6,2,7,0,9,8]

sorted_list = []

def checking_element(idx,val):
    global sorted_list
    if idx < 0:
        temp_list_1 = [val]
        sorted_list = temp_list_1 + sorted_list
        return sorted_list
    if idx == 0 and len(sorted_list) == 0:
        print("Test1")
        sorted_list.append(list[idx])
        return sorted_list
    else:
        print("Test2")
        if sorted_list[idx-1] <= val:
            print('1-', sorted_list)
            temp_list_1 = sorted_list[:idx]
            print('temp 1', temp_list_1)
            temp_list_1.append(val)
            print('temp 2', temp_list_1)
            try:
                temp_list_2 = sorted_list[idx:]
                sorted_list = temp_list_1 + temp_list_2
            except:
                sorted_list = temp_list_1
            print('2-', sorted_list)
            return sorted_list
        else:
            return checking_element(idx-1, val)
        
    
for i in range(len(list)):
    print(i)
    sorted_list = checking_element(i, list[i])
    print(sorted_list)
    
