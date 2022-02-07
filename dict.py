
def days_with_cond(num_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_days} days are {num_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_days} days are {num_days * 24 * 60} minutes"
    else :
        return "unsupported units"    

def try_and_excpet():
    
    # user_input1 = input("Enter a number\n")
    try:
        user_input_int1 = int(days_and_unit_dict["days"])
        if user_input_int1 > 0:
            cond_days = days_with_cond(user_input_int1, days_and_unit_dict["unit"])
            print(cond_days)
            # print("Condtional statement")
        elif user_input_int1 == 0:
            print("Enter a value greater then 0")
        else:
            print("Enter a positive number")
    except ValueError:
        print(" Enter a Valid number positive number")        

user_input1 = ""
while user_input1 != "exit":
    user_input1 = input("Enter a number of days and unit for conversion\n")
    days_and_unit = user_input1.split(":")
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    try_and_excpet()
    