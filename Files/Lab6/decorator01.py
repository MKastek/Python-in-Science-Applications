# Decorator


def called_decorator(func):
    def wrapper(*args, **kwargs):
        print("Called")
        return func(*args, **kwargs)
    return wrapper


@called_decorator
def fibon(n):
    return f'Hello fibon = {n}'


print(fibon(15))
