# raise error by hand

while True:
    try:
        age = int(input("How old are you? Input here: "))
        10/age  # 0 inputed but doesn't work.
        print(age)
    except ZeroDivisionError:
        raise ValueError("You are just a little baby. Call your mom!")
    except ValueError:
        print("Please Enter a Number.")
    else:  # if there is no error.
        print("Thank you.")
        break
    finally:
        print(":)")

# break and continue.

while True:
    try:
        age = int(input("How old are you? Input here: "))
        10/age  # 0 inputed but doesn't work.
        print(age)
    except ZeroDivisionError:
        print("Please enter a number higher than 0.")
        break
    except ValueError:
        print("Please Enter a Number.")
        continue
    else:  # if there is no error.
        print("Thank you.")
        break
    finally:
        print(":)")
    print("Can you hear me ?")  # this is never got be ran.


# finally

while True:
    try:
        age = int(input("How old are you? Input here: "))
        10/age  # 0 inputed but doesn't work.
        print(age)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Sth goes wrong.{e}")
    else:  # if there is no error.
        print("Thank you.")
        break
    finally:
        print(":)")

# Save the errors in (), and print them.

while True:
    try:
        age = int(input("How old are you? Input here: "))
        10/age  # 0 inputed but doesn't work.
        print(age)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Sth goes wrong.{e}")
    else:  # if there is no error.
        print("Thank you.")
        break


# different types of errors.

while True:
    try:
        age = int(input("How old are you? Input here: "))
        10/age  # 0 inputed but doesn't work.
        print(age)
    except ZeroDivisionError:
        print("Please enter a number higher than 0.")
    except ValueError:
        print("Please Enter a Number.")
    else:  # if there is no error.
        print("Thank you.")
        break


# simple way

while True:
    try:
        age = int(input("How old are you? Input here: "))
        0/age  # 0 inputed but doesn't work.
        print(age)
    except Exception:
        print("Please inter a Number.")
    else:  # if there is no error.
        print("Thank you.")
        break
