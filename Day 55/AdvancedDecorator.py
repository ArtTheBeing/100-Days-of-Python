class User:
    def __init__(self, name):
        self.name = name
        self.logged = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs): #The args and kwargs are actually the functions inputs
        if args[0].logged == True: 
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User('Daniel')
new_user.logged = True
create_blog_post(new_user)