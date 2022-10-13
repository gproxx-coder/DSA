class InvalidAgeException(Exception):
    def __init__(self, msg="Age cannot be less than zero", *args):
        super(InvalidAgeException, self).__init__(msg, *args)


def age_validator(func):
    def inner(age):
        if age < 0:
            raise InvalidAgeException
        func(age)

    return inner


@age_validator
def print_age(age):
    print("Age is", age)


print_age(55)

print_age(0)

print_age(-5)
