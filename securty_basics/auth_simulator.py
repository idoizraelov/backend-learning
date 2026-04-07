import bcrypt


def register(password):

    #Change string to bytes
    pass_bytes = password.encode('utf-8')
    #Create a random string
    salt = bcrypt.gensalt()
    #Mix password and string to make the hash
    hashed_password = bcrypt.hashpw(pass_bytes, salt)

    return hashed_password

#Check if the user password matches the saved hash
def login(password, saved_hash):
    #Change the entered password to bytes
    pass_bytes = password.encode('utf-8')

    return bcrypt.checkpw(pass_bytes, saved_hash)

def input_pass():
    print('Enter your password: ')
    print("Rules: ")
    print("Password must have at least 8 characters")
    print("Password must have at least 1 capital letter.")
    print("Password must have at least 1 number.")
    print("Password must have at least 1 special character like-> !@#$%^&*_")
    while (True):
        password = input("\nPassword: ")
        # Rule 1: Length
        if len(password) <8:
            print("Password too short. Try again.")
            continue
        # Rule 2: Uppercase
        upper= any(c.isupper() for c in password)
        if not upper:
            print("Password must have at least one uppercase letter. Try again.")
            continue
        # Rule 3: Number
        number = any(c.isdigit() for c in password)
        if not number:
            print("Password must have at least one number. Try again.")
        # Rule 4: Special Character
        special_characters = "!@#$%^&*_"
        has_special = any(c in special_characters for c in password)

        if not has_special:
            print("Password must have at least one special character (!@#$%^&*_). Try again.")
            continue

        print("The password is valid.")
        return password


# Testing the Code
def main():
    my_password = input_pass()

    # Save the result in our "database"
    saved_db_hash = register(my_password)
    print("Saved Hash:", saved_db_hash)

    attempts=0
    max_attempts=3
    is_logged_in = False

    while attempts < max_attempts:
        login_guess = input("Please enter your login password: ")

        ans_correct = login(login_guess, saved_db_hash)
        if not ans_correct:
            attempts += 1
            print(f"Wrong password. You have {max_attempts - attempts} attempts left.")
            continue
        else:
            print("Login Successful! Welcome to the system.")
            is_logged_in = True
            break

    if not is_logged_in:
        print("ACCOUNT LOCKED! You made too many mistakes.")


main()

