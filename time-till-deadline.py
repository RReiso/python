import datetime

user_input = input("Enter your goal with a deadline seperated by colon\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

# convert string to date in the specified format
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
# first datetime  - module name because of the import, second datetime - class name

# calculate days from now till the deadline:
today_date = datetime.datetime.today()
days_till_deadline = deadline_date - today_date

print(f"Time remaining in: {days_till_deadline.days}")
