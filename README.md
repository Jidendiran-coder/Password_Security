# 🔐 Password Strength Checker

## 📌 Project Description
A simple Python script that evaluates the strength of a user-entered password based on predefined security criteria. The script checks for length, uppercase and lowercase letters, numbers, and special characters to ensure strong password security.

## 📖 Table of Contents
1. [⚙️ Prerequisites](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#%EF%B8%8F-prerequisites)
2. [📥 Installation Instructions](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-installation-instructions)
3. [📝 Usage Instructions](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-usage-instructions)
4. [🔧 Configuration](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-configuration)
5. [🚀 CI/CD Pipeline Details](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-cicd-pipeline-details)
6. [🔒 Security Best Practices](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-security-best-practices)
7. [🐞 Troubleshooting](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-troubleshooting)
8. [🤝 Contribution Guidelines](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-contribution-guidelines)
9. [📜 License](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-license)
10. [📸 Screenshots & Architecture Diagrams](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-screenshots--architecture-diagrams)
11. [📅 Changelog](https://github.com/Jidendiran-coder/Password_Security?tab=readme-ov-file#-changelog)

## ⚙️ Prerequisites
- 🐍 Python 3.x installed on your system
- 🔗 `stdiomask` module installed (to securely mask password input)

## 📥 Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-strength-checker
   ```
3. Install dependencies:
   ```bash
   pip install stdiomask
   ```

## 📝 Usage Instructions
1. Run the script:
   ```bash
   python password_checker.py
   ```
2. Enter a password when prompted. The script will evaluate its strength and display feedback.

## 🔧 Configuration
- Modify the `testpass` function to add/remove security rules as needed.

## 🚀 CI/CD Pipeline Details
- This project can be integrated into a CI/CD pipeline for automated security checks.
- Consider using GitHub Actions for automated testing.

## 🔒 Security Best Practices
- ❌ Do not log passwords in plaintext.
- 🔑 Use environment variables for password policies.
- 🛡️ Consider implementing additional security measures, such as password hashing.

## 🐞 Troubleshooting
- If `stdiomask` is not installed, run:
  ```bash
  pip install stdiomask
  ```

## 🤝 Contribution Guidelines
- 🔀 Fork the repository and submit a pull request with your improvements.

## 📜 License
This project is licensed under the MIT License.

## 📸 Screenshots
a) When we Provde a WEAK password:
![image](https://github.com/user-attachments/assets/08d9a568-e7b0-48c3-af3f-1292cc43eb4a)

b) When we provide a STRONG password:
![image](https://github.com/user-attachments/assets/f6487224-6d30-409b-b5bd-80b9cf2c1a51)


## 📅 Changelog
- **v1.0** - Initial release with basic password validation.

