import pdb

def mean(nums):

    bot = len(nums)
    it = 0
    top = 0
    while it < len(nums):
	top += nums[it]
        it += 1
    return float(top)/bot

a_list = [1,2,3,4,5]

pdb.set_trace()
print(mean(a_list))

