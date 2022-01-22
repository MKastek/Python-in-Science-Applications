def my_function_a():
    print(f'Hello  from package: {__name__}')

#utility function
def my_function_b():
    print(f'Hello  from package: {__name__}')


#zmienna mówiąca co będzie importowane publicznie

__all__ = ['my_function_a']