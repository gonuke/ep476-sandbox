import math


multiplier = 12

def mean(list_of_numbers):

   multiplier = 10

   mn = float(sum(list_of_numbers))/len(list_of_numbers)
   return mn*multiplier

def stdev(list_of_numbers):

   mn = mean(list_of_numbers)

   sd = 0
   for number in list_of_numbers:
       sd = sd + (number - mn)*(number - mn)

   sd = sd/len(list_of_numbers)
   return math.sqrt(sd)

def line(x,m=1.0,b=0):
    return m*x + b


a_list = [1,2,3,4]


print(mean(a_list))
print(stdev(a_list))


print(line(5))
print(line(5,2))
print(line(5,b=2))
print(line(5,m=2))


def minimum(*args):
    m = args[0]
    for val in args[1:]:
        if val < m:
           m = val
    return m

print( minimum(1,5,-9.6,-5))


def minmax(*args):
    mn = args[0]
    mx = args[0]
    for val in args[1:]:
        if val < mn:
           mn = val
        if val > mx:
           mx = val
	
    return mn, mx, mn+mx

my_min, my_max, my_mm_sum =  minmax(1, -8, 12, -4)

print("my_min: " + str(my_min) + ", my_max: " + str(my_max))






    
