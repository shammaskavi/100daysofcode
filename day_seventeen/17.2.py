class User:
    def __init__(self, user_id, username):
        print("New user being Created.")  
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "Jack")
print(f"The user {user_1.username} has {user_1.following} following and {user_1.followers} followers.")
user_1.follow(user_2)
print(f"The user {user_1.username} has {user_1.following} following and {user_1.followers} followers.")
print(f"The user {user_2.username} has {user_1.following} following and {user_2.followers} followers.")
