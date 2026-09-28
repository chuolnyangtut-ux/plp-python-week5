import random
import string


def make_password(length=8):
    """Generates a random password consisting of ascii letters and digits.

    Parameters:
        length (int): Length of the password (defaults to 8).

    Returns:
        str: Randomly generated password.
    """
    characters = string.ascii_letters + string.digits
    password = ""

    # Loop to add one random character at a time
    for i in range(length):
        password += random.choice(characters)

    return password


p1 = make_password()
p2 = make_password(12)

print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))