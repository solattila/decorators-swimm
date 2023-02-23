def logger(function):
    def wrapper(*args, **kwargs):
        print(f"Function {function.__name__} was called")
        result = function(*args, **kwargs)
        print(f"Function {function.__name__} returned with {result}")
        print("really cool")
        return result
    return wrapper

@logger
def add_two_numbers(a, b):
    return a + b


if __name__ == "__main__":
    add_two_numbers(3, 5)