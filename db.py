import hashlib
import binascii
import os
import sqlite3
from sqlite3 import Connection

path = os.path.abspath(os.path.dirname(__file__))


def init_db():
    os.makedirs(path+"/databases")
    con = sqlite3.connect(path+"/databases/user_accounts.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE users(email, password)")
    con.commit()
    con.close()


# https://www.vitoshacademy.com/hashing-passwords-in-python/
# Thanks for the password hashing tutorial; Thought me alot on how to properly hash password and use salts
def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password






def register_user(email: str, password: str) -> bool:
    # Wrapping in try / except just in case something goes wrong
    if email == "" or password == "": return False
    try:
        con = sqlite3.connect(path + "/databases/user_accounts.db")
        con.cursor().execute("INSERT INTO users VALUES(?,?)",
                             (email, hash_password(password=password)))
        con.commit()
        con.close()
    except Exception:
        return False
    return True
def login_user(email: str, password: str) -> bool:
    if email == "" or len(password) <= 7: return False
    con = sqlite3.connect(path + "/databases/user_accounts.db")
    cur = con.cursor()
    # Searching for all users that are registered with given email
    cur.execute("SELECT password FROM USERS WHERE EMAIL = ?", (email,))
    # Fetching all users and getting their password
    db_password = cur.fetchall()
    con.close()
    return verify_password(db_password[0][0], password)


def user_exists() -> bool:
    con = sqlite3.connect(path + "/databases/user_accounts.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS")
    if cur.fetchall() == []:
        return False
    return True


# Running if library gets imported
if not os.path.exists(path=path+"/databases"):
    init_db()