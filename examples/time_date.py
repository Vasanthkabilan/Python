from datetime import datetime

user_input = input("Enter your goal with a deadline\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
actual_time = deadline_date - today_date

print(f"Time remaining for your goal: {goal} is {actual_time.days} days")