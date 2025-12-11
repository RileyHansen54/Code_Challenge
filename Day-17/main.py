

class User:
    def __init__(self, user_id,name):
        self.id = user_id
        self.username = name
        self.followers = 0
        self.following = 0
       
    def follow(self,user):
        user.followers +=1
        self.following += 1
       
user1 = User(1, "Riley")
user2 = User(2, "Lara")



user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following,"\n")
user2.follow(user1)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)




