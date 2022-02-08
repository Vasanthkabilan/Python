from user import User
from post import Post

app_user_one = User("vv@vv.com", "Vasanth", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

new_post = Post("I am learning Python", app_user_one.name)
new_post.get_post_info()