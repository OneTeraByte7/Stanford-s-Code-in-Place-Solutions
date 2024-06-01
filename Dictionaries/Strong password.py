"""Question : Fill out the login(...) function for a website which hashes their passwords. Login should return True if an email's 
              stored password hash in stored_logins is the same as the hash of password_to_check.
"""

from hashlib import sha256

def login(email, stored_logins, password_to_check):
    if stored_logins[email] == hash_password(password_to_check):
        return True

    return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb",
        "sohamceengineer13@gmail.com":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
    }
    
    print(login("example@gmail.com", stored_logins, "word"))
    print(login("example@gmail.com", stored_logins, "password"))
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))
    print(login("code_in_placer@cip.org", stored_logins, "karel"))
    
    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "123!456?789"))
    
    print(login("sohamceengineer13@gmail.com", stored_logins, "123456"))
    print(login("sohamceengineer13@gmail.com", stored_logins, "173629"))
    

if __name__ == '__main__':
    main()