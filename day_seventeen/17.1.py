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
# user_1.id = "001"
# user_1.username = "angela"

print(user_1.username, user_1.id)
 

user_2 = User("002", "Jack")
# user_2.id = "001"
# user_2.username = "Jack"

print(user_2.username, user_2.id)