# importing module
import helper

# from helper import <function name>, <Variables> --- to call specific function or Variables
user_input1 = ""
while user_input1 != "exit":
    user_input1 = input("Enter a number of days and unit for conversion\n")
    days_and_unit = user_input1.split(":")
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    helper.try_and_excpet(days_and_unit_dict)