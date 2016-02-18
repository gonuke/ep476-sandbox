import sys

def look_in_list(find_number,search_list):
   print("Looking for " + str(find_number) + " in " + str(search_list))
   if find_number in search_list :
      print("It always is")
      return True
   elif 8 in search_list :
      print("At least the number 8 is.")
   else :
      print("I guess not!")
   return False

try:
   search_number = int(sys.argv[1])
except ValueError:
   print("Nice argument - but it needs to be an integer.")
   sys.exit()
except IndexError:
   print("You didn't provide enough arguments")
   sys.exit()
except:
   print("You need to provide an argument - which number should I look for in the list?")
   sys.exit()

my_list = [1, 2, 3, 4]

print(look_in_list(search_number,my_list))
print(look_in_list(search_number,[45, 23, 5, 8]))


msg = "It still is" if search_number in my_list else "Still can't find it"

print(msg)

count = 0
attention_span = 10

while count < search_number:
   print("Your number was not " + str(count))
   if count > attention_span: 
	print("I'm bored and giving up...")
	break
   count = count + 1
print("Your number WAS......" + str(count))


for count2 in range(attention_span):
   if (count2%2 == 0):
	continue
   print("Your number was not " + str(count2))
   
my_other_list = ["Paul", "Laurie", "Moira", "Rhiannon"]

for name in my_other_list:
   print(name + " is in my family.")
 

for person_id in range(len(my_other_list)):
   print(my_other_list[person_id] + " is in my family.")

sub_list = []

for number in my_list:
    sub_list.append(number*number)

print(sub_list)

square_list = [ number*number for number in my_list  ]

print(square_list)

dict_of_squares = { number : number*number for number in my_list }

print(dict_of_squares)

dict_of_even_squares = { number : number*number for number in my_list if number%2 == 0 }


print(dict_of_even_squares)

# my_file = open('lec09.py')

# for line in my_file:
#      print("my_file contains: |" + line + "|")














