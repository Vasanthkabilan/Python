class User:
    def __init__(self, user_email, name, password, job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.job_title = job_title
    
    def change_password(self, new_password):
        self.password = new_password
    
    def change_title(self, new_job_title):
        self.job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently work as an {self.job_title}. You can contact him in {self.email}")

