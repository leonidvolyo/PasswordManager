import string
import secrets
from mysql.connector import connect, Error

def connect_to_db():    ### Исправить: доделать отключение (было реализовано с помощью With & ContextManager
    try:
        connection = connect(
           host="YOU NEED YOUR OWN DB SERVER",
           user = "YOU NEED YOUR OWN DB SERVER",
           #user=input("Enter username: "),
           password="YOU NEED YOUR OWN DB SERVER",
           database="YOU NEED YOUR OWN DB",
        )
        return connection
    except Error as e:
        print(e)

def add_password(service_name, password):
    insert_password_query = """INSERT INTO passwords (service_name, password) VALUES (%s, %s)"""
    data_to_insert = (service_name, password)
    connection = connect_to_db()
    with connection.cursor() as cursor:
        cursor.execute(insert_password_query, data_to_insert)
        connection.commit()

def generate_new_password(passlen):
    letters_digits_punc = string.ascii_letters + string.digits + "(,._-*~<>/|!@#$%^&)+="
    return "".join(secrets.choice(letters_digits_punc) for i in range(passlen))

def delete_password(service_name):
    delete_password_query = """DELETE FROM passwords WHERE service_name = %s"""
    connection = connect_to_db()
    with connection.cursor() as cursor:
        cursor.execute(delete_password_query, service_name)
        connection.commit()

def find_password(service_name):
    find_password_query = """SELECT password FROM passwords WHERE service_name = %s;"""
    connection = connect_to_db()
    with connection.cursor(buffered=True) as cursor:
        """cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
        connection.commit()"""
        cursor.execute(find_password_query, [service_name])
        connection.commit()
        result = cursor.fetchone()
        return(bytes(result[0]))

"""print(find_password("d"))"""


# TAK RABOTAET
"""new_pass = Manager()
print(new_pass.generate_new_password(8))
"""
# A TAK NE RABOTAET: (NAVERNOE SNACHALA SOZDAT OBJEKT, A POTOM UZE OBRASHATSYA K NEMU)
# print(Manager.generate_new_password(8))



