import re  # 🔍 Importing the regular expressions module for pattern matching
import stdiomask  # 🔒 Importing stdiomask to securely mask user input while typing

def testpass(password):
    """
    🛡️ Function to check the strength of a password based on the following conditions:
    ✅ Minimum length of 8 characters
    ✅ At least one uppercase letter (A-Z)
    ✅ At least one lowercase letter (a-z)
    ✅ At least one digit (0-9)
    ✅ At least one special character (~!@#$%^&*()<>?/:;'[]{})
    
    Parameters:
        🔑 password (str): The password entered by the user

    Returns:
        🎯 bool: True if the password meets all criteria, otherwise False
    """
    if len(password) < 8:
        return False  # ❌ Password must be at least 8 characters long
    if not re.search(r"[A-Z]", password):
        return False  # ❌ Password must contain at least one uppercase letter 🔠
    if not re.search(r"[a-z]", password):
        return False  # ❌ Password must contain at least one lowercase letter 🔡
    if not re.search(r"[0-9]", password):
        return False  # ❌ Password must contain at least one digit 🔢
    if not re.search(r"[~!@#$%^&*()<>?/:;'{[\]}]+", password):
        return False  # ❌ Password must contain at least one special character 💥
    return True  # ✅ If all conditions are met, return True (Strong Password) 🔥

def main():
    """
    🎯 Main function to prompt the user for a password and check its strength.
    If the password meets all security requirements, it is considered strong. 💪
    Otherwise, a warning message is displayed with improvement suggestions. ⚠️
    """
    print("\n🔐 Welcome to the Password Strength Checker! 🔐\n")  
    password = stdiomask.getpass(prompt="📝 Enter a Password to check its strength: ", mask='*')  # Securely take password input
    if testpass(password):
        print("✅ The password is strong! 🔥🔒")  # If password meets all conditions
    else:
        print("\n🚨 The password is weak! 🚨\n")
        print("🔴 Requirements for a strong password:")
        print("  🔹 At least 8 characters long")
        print("  🔹 Contains both uppercase (A-Z) and lowercase (a-z) letters")
        print("  🔹 Includes at least one digit (0-9) 🔢")
        print("  🔹 Must have at least one special character (~!@#$%^&*...) 💥")
        print("\n⚠️ Please try again with a stronger password! 🔁\n")  

# Ensuring that the script runs only when executed directly, not when imported as a module
if __name__ == "__main__": 
    main()  # 🚀 Start the password strength checker!

