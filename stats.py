def median(nums):

    nums = list(nums)

    nums.sort()   

    if len(nums)%2 == 0:
	return mean(nums[len(nums)/2-1:len(nums)/2+1])
    else:
        return nums[len(nums)/2]



def mean(nums):

    try:
        num_vals = len(nums)
    except TypeError:
	return nums

    try:
        ret_val = float(sum(nums))/len(nums)
    except ZeroDivisionError:
        return None

    return ret_val

