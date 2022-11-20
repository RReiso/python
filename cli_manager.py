from dateutil.parser import parse
from datetime import datetime
import requests
from requests.exceptions import HTTPError


class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'


class Manager:
    def __init__(self):
        self.REMINDER_WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/......"
        self.CALENDAR_WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/......"
        self.OPTIONS = ["1", "2", "3", "4", "5", "6"]

    def start_manager(self):
        print(f"{bcolors.YELLOW}Welcome to your personal manager app!\n")
        self.show_options()

    def show_options(self):
        print(
            f"{bcolors.BLUE}What would you like to do? Enter a number!\n" + bcolors.ENDC)
        print("""1. Set a reminder
2. Read my notes
3. Add a note
4. Delete my notes
5. Create a calendar event
6. Exit\n""")

        choice = ""
        while choice not in self.OPTIONS:
            choice = input("Your choice: ")

        match choice:
            case "1":
                self.set_reminder()
            case "2":
                self.read_notes()
            case "3":
                self.add_note()
            case "4":
                self.delete_notes()
            case "5":
                self.create_event()
            case "6":
                self.exit_program()

    def set_reminder(self):
        reminder = input("Reminder: ")

        while True:
            reminder_datetime = self.get_datetime()
            now = datetime.now()
            diff_days = (reminder_datetime.date() - now.date()).days

            # check if datetime is in the future but not more than one month ahead (=> Zap error)
            if now >= reminder_datetime:
                print("Please, set a future date and time!")
            elif diff_days > 30:
                print("Dates cannot be more than a month in the future")
            else:
                break

        message = {"reminder": reminder, "date_time": reminder_datetime}
        self.send_msg_to_webhook(message, self.REMINDER_WEBHOOK_URL)

    def create_event(self):
        while True:
            calendar_datetime = self.get_datetime()
            now = datetime.now()

            if now > calendar_datetime:
                print("Please, set a future date and time!")
            else:
                break

        description = input("Description: ")
        message = {"date_time": calendar_datetime, "description": description}
        self.send_msg_to_webhook(message, self.CALENDAR_WEBHOOK_URL)

    def get_datetime(self):
        date_time = ""
        while not date_time:
            date_time = input("Date and time: ")
            if self.is_date(date_time):
                date_time = parse(date_time)
            else:
                date_time = ""
        return date_time

    def is_date(self, string):
        try:
            parse(string)
            return True
        except ValueError:
            return False

    def send_msg_to_webhook(self, message, url):
        try:
            res = requests.post(url, data=message)
            # If the response was successful, no Exception will be raised
            res.raise_for_status()
            print(f"{bcolors.GREEN}Success!" + bcolors.ENDC)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        self.continue_or_exit()

    def read_notes(self):
        print(
            f"\n{bcolors.GREEN}Your notes:" + bcolors.ENDC)
        with open("notes.txt", 'r') as notes:
            print(notes.read(), '\n')
        self.continue_or_exit()

    def add_note(self):
        note = input("Note: ")
        with open("notes.txt", 'a') as notes:
            notes.write("\n" + note)
        print(f"{bcolors.GREEN}Note added!\n" + bcolors.ENDC)
        self.continue_or_exit()

    def delete_notes(self):
        with open("notes.txt", 'w') as notes:
            notes.write("")
        print(f"{bcolors.GREEN}Notes deleted!\n" + bcolors.ENDC)
        self.continue_or_exit()

    def continue_or_exit(self):
        YES_NO = ["y", "n", "yes", "no"]
        choice = ""
        while choice not in YES_NO:
            choice = input("Show options? y/n: ").lower()

        if choice in ["y", "yes"]:
            self.show_options()
        else:
            self.exit_program()

    def exit_program(self):
        print(f"{bcolors.YELLOW}See you next time, bye!")
        exit


manager = Manager()
manager.start_manager()
