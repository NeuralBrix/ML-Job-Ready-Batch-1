# name = input("Give your name: ")
# print(f"your name is: {name}")

# first_name = input("Give your first name: ")
# last_name = input("Give your last name: ")
# full_name = first_name + " "+ last_name 
# print(f"your name full name is: {full_name}")

# first_number = int(input("Give your first number: "))
# last_number = float(input("Give your last number: "))
# add_result = first_number + last_number 
# print(f"Your addition result is: {add_result}")


first_name, last_name = input("Give your full name: ").split(" ") #("mehedi","Hasan")
full_name = first_name + " "+ last_name 
print(f"your name full name is: {full_name}")