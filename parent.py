
local_val = "magical unicorns"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name

    # creating a method to greet the user 
    def say_hello(self):
        return "hello"

# in the same file, add the following below the User class
print(square(5))

# instantiating a user 
user = User("Anna")
print(user.name)
print(user.say_hello())

# checking the variables that are avaialble in the current Namespace
    # print(locals())

# checking the file created __name__ 
    # print(__name__)
    
if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)