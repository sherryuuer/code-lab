# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrap_func(*args, **kwargs):
        if args[0]['valid']:
            fn(*args, **kwargs)
        else:
            print("Kick you off.")
    return wrap_func
# why args?


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
