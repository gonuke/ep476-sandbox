import sys

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

print("Looking for " + str(search_number) + " in " + str(my_list))

if search_number in my_list :
   print("It always is")
elif 8 in my_list :
   print("At least the number 8 is.")
else :
   print("I guess not!")

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













