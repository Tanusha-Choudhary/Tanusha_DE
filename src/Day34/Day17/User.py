class User:
    # First letter capital and ther small (PascalCase)-> PASCAL CASE
    # CAMELCASE ( camelCase)
    # SNAKE_CASE(snake_case)
    def __init__(self,id,key):
        self.username = id
        self.password = key
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following+=1
user1 = User("user1","pass1")
user2 = User("user2","pass2")
# print(user1.username,user1.password)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)