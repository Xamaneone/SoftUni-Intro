from custom_exceptions import NameTooShort, MustContainAtSymbolError, InvalidDomainError
from helpers import VALID_DOMAIN

def valid_email(email):
    try:
        name, domain = email.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")
    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")
    try:
        name, extension = domain.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if extension not in VALID_DOMAIN:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    return True



email = input()

while email != "End":

    if valid_email(email):
        print("Email is valid")


    email = input()