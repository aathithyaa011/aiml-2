# A simple Python program
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)