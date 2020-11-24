class User:
    """
    this is User Class
    """

    name = 'UserClass'
print(type(User))
print(User.__doc__)
user = User()
new_list = list()

print(type(user))

print(user.name)

user.name = 'harry'
print(user.name)
print(User.name)