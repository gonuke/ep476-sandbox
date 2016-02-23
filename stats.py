def mean(nums):

    try:
        num_vals = len(nums)
    except TypeError:
	return nums

    try:
        ret_val = float(sum(nums))/len(nums)
    except ZeroDivisionError:
        return None
    except TypeError:
	return NotImplemented

    return ret_val

