# # variables
# # I/O is E/S in portuguese
# # string formatting
#
# age = 18 # int
# age_cousin = 20 # int
# distance_next_town = 15.2 # float
# name = 'Daniel' # str
# other_name = "Test" # str
# cold = True # bool
#
# print(distance_next_town * 2)
# input_string = input("Type something in: ")

age = input("Type in your age: ")
age_cousin = input("Type in your cousin's age: ")
if age > age_cousin:
    print("You are older than your cousin.")
elif age_cousin > age:
    print("Your cousin is older than you.")
elif age_cousin == age:
    print("You and your cousin have the same age.")
else:
    print("Undefined")