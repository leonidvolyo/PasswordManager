import hashlib
import os

class Users:
    __master_users = {}
    def user_append(self, username, key, salt):
        self.__master_users[username] = {"key": key, "salt": salt}
    def get_master_users(self):
        return self.__master_users

user = Users()

def add_user(username, password):
    salt = os.urandom(32)  # New salt for this user (without using pseudo...)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    user.user_append(username, key, salt)

    """salt = os.urandom(32)  # New salt for this user (without using pseudo...)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    master_users[username] = {
       'salt': salt,
       'key': key
    }"""


# Function will return true if entered key = original key
def check_master_password(username, master_password):
    salt = user.get_master_users()[username]['salt']  # Получение соли
    key = user.get_master_users()[username]['key']  # Получение правильного ключа
    new_key = hashlib.pbkdf2_hmac('sha256', master_password.encode('utf-8'), salt, 100000)
    return key == new_key

def hashing_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key, salt


