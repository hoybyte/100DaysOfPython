from functools import wraps


def your_decorater(func):
    '''Decorator to...'''
    @wraps(func) # preserves function meta data
    def wrapper(*args, **kwargs):
        # do stuff before function
        return func(*args, **kwargs)
        # do stuff after function
    return wrapper


@your_decorater
def some_function():
    pass

if __name__ == '__main__':
    some_function()