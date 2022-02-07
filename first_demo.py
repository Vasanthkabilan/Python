# Defining a Variable
day_min = (24 * 60)

# Defining a function:


def days_to_unit():
    print(f"20 days are {20 * day_min} minutes for function example")
    print("Function example")

# Calling a function:

days_to_unit()

# def function with parameters | with custom message


def days_with_para(num_days , custom_message):
    print(f"{num_days} days are {num_days * day_min} minutes")
    print(custom_message)

# Calling a function:


days_with_para(20 , "Function with parameters")

# def function with return value


def days_with_ret(num_days):
    return(f"{num_days} days are {num_days * day_min} minutes")

# Validating user input
user_input = input("Enter a number for validating user input is digit\n")
if user_input.isdigit():
    user_input_int = int(user_input)
    ret_days = days_with_ret(user_input_int)
    print(ret_days)
    print("Function with return value")
else:
   print("Enter a Interger Value") 

# Example for conditional statement
def days_with_cond(num_days):
    return(f"{num_days} days are {num_days * day_min} minutes")

# Example for conditional statement | Nested statement
# User input Validation into the function:
def validate_and_execute():
    
    user_input1 = input("Enter a number for validation with nested concept\n")

    if user_input1.isdigit():
        user_input_int1 = int(user_input1)
        if user_input_int1 > 0:
            cond_days = days_with_cond(user_input_int1)
            print(cond_days)
            print("Conditional statement")
        elif user_input_int1 == 0:
            print("Enter a value greater then 0")
    else:
        print("Enter a Integer")

validate_and_execute()

# Try and except validation | # While loop concept | For loop | List


def try_and_excpet():
    
    # user_input1 = input("Enter a number\n")
    try:
        user_input_int1 = int(num_of_days_while)
        if user_input_int1 > 0:
            cond_days = days_with_cond(user_input_int1)
            print(cond_days)
            # print("Condtional statement")
        elif user_input_int1 == 0:
            print("Enter a value greater then 0")
        else:
            print("Enter a positive number")
    except ValueError:
        print(" Enter a Valid number positive number with comma or a single value")        

user_input1 = ""
while user_input1 != "exit":
    user_input1 = input("Enter a number with comma or single value for loop and list concept\n")
    for num_of_days_while in user_input1.split(","):    
        try_and_excpet()


