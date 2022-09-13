import argparse

parser = argparse.ArgumentParser(description="lala lala")
parser.add_argument(
    'fname',
    type=str,
    help="Enter your first name"
)

parser.add_argument(
    '-lname',
    '--last_name',
    type=str,
    help="enter your last name"
)

args = parser.parse_args()
first_name = args.fname
last_name = args.last_name if args.last_name else ""
print("Hello {} {}!".format(first_name, last_name))

# python3 password.py John -ln Doe
# python3 password.py John --last_name Doe
