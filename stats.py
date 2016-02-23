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

