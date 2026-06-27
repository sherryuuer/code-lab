# # Higher order function.
# WHAT if this great decorator
def my_final_decorator(func):
    def wrap_function(*args, **kwargs):
        print("xxxxxsunnydayxxxxx")
        func(*args, **kwargs)
        print("xxxxxhappydayxxxxx")
    return wrap_function

# decorator without para
# def my_decorator(func):
#     def wrap_function():
#         print("xxxxxsunnydayxxxxx")
#         func()
#         print("xxxxxhappydayxxxxx")
#     return wrap_function


def simple_hello():
    print("Hello")


@my_final_decorator
def simple_bye():
    print("Bye")


# They will perform the same
a = my_final_decorator(simple_hello)
a()

simple_bye()

# -----------------------------------
# what if with parameters
# def my_decorator(func):
#     def wrap_function(name):
#         print("xxxxxsunnydayxxxxx")
#         func(name)
#         print("xxxxxhappydayxxxxx")
#     return wrap_function


def hello(name):
    print(f"Hello, {name}")


@my_final_decorator
def bye(name):
    print(f"Bye, {name}")


# They will perform the same
a = my_final_decorator(hello)("Dan")
# or a("Dan")

bye("Dan")

# finally use ** parameter
