from user import User

first_user = User("example@example.com", "John Doe", "1234", "developer")
first_user.get_user_info()
first_user.change_job_title("software developer")
first_user.get_user_info()
