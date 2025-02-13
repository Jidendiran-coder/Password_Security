import re
import stdiomask

def testpass(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[~!@#$%^&*()<>?/:;'{[\]}]+", password):
        return False
    return True

def main():
    print("\n")
    password = stdiomask.getpass(prompt="Enter a Password to check its strength: ", mask='*')
    if testpass(password):
        print("The password is strong.")
    else:
        print("\nThe password is weak.\n  > It must be at least 8 characters long\n  > Contain both uppercase and lowercase letters\n  > At least one digit\n  > And at least one special character")
        print("\nPlease try again...\n")
        
if __name__ == "__main__": 
    main()