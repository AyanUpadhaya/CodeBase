# Binary Search using Python
#=======================================================
# as your list length increases time increases as well

# in binary search all the values have tobe sorted 

# first specify the lower bound which is list[0] index

# then specify the upper bound which is last element len(list) -1

# get mid index = lower+upper/2 -> (0+5)/2 = 2_

# check if the mid value is matching with search element

# change lower bound or upper bound for the next iteration

# check if the value you are searching for is bigger or smaller than mid value

# if the value is smaller change the upper bound which means the mid value is the new upper bound

# if the value is greater than change the lower bound which means the mid value is the new lower bound

# it will improove the speed

pos = -1
nums = [4,7,8,12,45,99,100]

n = 100

def search(numlist,n):
    lowerbound = numlist[0]
    upperbound = len(numlist) - 1
    while lowerbound <= upperbound:
        mid = (lowerbound+upperbound)//2
        if numlist[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if numlist[mid] < n:
                lowerbound = mid+1
            else:
                upperbound = mid-1
    return False

if search(nums,n):
    print("Found at ",pos+1)
else:
    print('Not found')
     
