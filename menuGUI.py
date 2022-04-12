import PySimpleGUI as sg
import hash
import cryptography_management
import password_manager

def first_window():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("Hello! Did you register your account before?")],
        [sg.Button("YES"), sg.Button("NO")],
        [sg.Button("EXIT")]
    ]
    window = sg.Window("Welcome to Password Manager", layout)
    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        elif event == "YES":
            welcome_window()
        elif event == "NO":
            add_new_user_window()
    window.close()

def add_new_user_window():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("Please, enter USERNAME and PASSWORD")],
        [sg.Text("USERNAME: "), sg.InputText(key='INPUT MASTER USERNAME')],
        [sg.Text("PASSWORD: "), sg.InputText(key='INPUT MASTER PASSWORD')],
        [sg.Button("OK"), sg.Button("EXIT")]
    ]
    window = sg.Window("New user registration", layout)
    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        elif event == "OK" and values['INPUT MASTER USERNAME'] != '' and values['INPUT MASTER PASSWORD'] != '':
            hash.add_user(values['INPUT MASTER USERNAME'], values['INPUT MASTER PASSWORD'])
            break
        elif event == "OK" and (values['INPUT MASTER USERNAME'] == '' or values['INPUT MASTER PASSWORD'] == ''):
            error_window()
    window.close()


def welcome_window():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("Good day, Sir! Please, Enter the password:")],
        [sg.InputText(key="USERNAME")],
        [sg.InputText(key="MASTER_PASS", password_char='*')],
        [sg.Button("Confirm"), sg.Button("Exit")]
    ]
    window = sg.Window("Welcome window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Confirm":
            if values['USERNAME'] in hash.user.get_master_users().keys():
                if hash.check_master_password(values['USERNAME'], values['MASTER_PASS']):
                    main_window()
                else:
                    error_window()
            else:
                error_window()
    window.close()



def main_window():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("Enter service name, please: ")],
        [sg.InputText(key='SERVICE')],
        [sg.Button("FIND PASSWORD"), sg.Button("ADD PASSWORD"), sg.Button("DELETE PASSWORD")],
        [sg.Button("EXIT")]
    ]
    window = sg.Window("PASSWORD MANAGER", layout)
    while True:
        event, values = window.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        elif event == "FIND PASSWORD":
            if password_manager.find_password(values['SERVICE']):
                found_password_window(values['SERVICE'])
            else:
                error_window()
        elif event == "ADD PASSWORD":
            adding_password_window(values['SERVICE'])
        elif event == "DELETE PASSWORD":
            if password_manager.find_password(values['SERVICE']):
                password_manager.delete_password(values['SERVICE'])
            else:
                error_window()
    window.close()



def ok_window():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("YOU MADE IT!")],
        [sg.Button("OK")]
    ]
    window = sg.Window("OK WINDOW", layout)
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break
    window.close()



def error_window():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("SORRY. INCORRECT OR EMPTY INPUT")],
        [sg.Button("OK")]
    ]
    window = sg.Window("ERROR WINDOW", layout)
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break
    window.close()



def found_password_window(service_name):
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("Password for Service " + service_name)],
        [sg.Text(cryptography_management.decryption(password_manager.find_password(service_name)))],
        [sg.Button("OK"), sg.Button("CLOSE")]
    ]
    window = sg.Window("Password for entered service", layout)
    while True:
        event, values = window.read()
        if event == "OK" or event == "CLOSE" or event == sg.WIN_CLOSED:
            break
    window.close()



def adding_password_window(service_name):
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("Create new password for chosen service, please: ")],
        [sg.InputText(key = 'NEW_PASSWORD'), sg.Button("OK")],
        [sg.InputText("or")],
        [sg.InputText(key = 'PASSLEN'), sg.Button("GENERATE NEW SAFE PASSWORD AUTOMATICALLY")],
        [sg.Button("CLOSE")]
    ]
    window = sg.Window("Adding new password", layout)
    while True:
        event, values = window.read()
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break
        elif event == "OK" and values['NEW_PASSWORD'] != "":
            key = cryptography_management.encryption(values['NEW_PASSWORD'].encode(encoding="UTF-8"))
            password_manager.add_password(service_name, key)
            ok_window()
        elif event == "OK" and values['NEW_PASSWORD'] == "":
            error_window()
        elif event == "GENERATE NEW SAFE PASSWORD AUTOMATICALLY" and values['PASSLEN'].isdigit() and int(values['PASSLEN']) > 0:
            generated_password = password_manager.generate_new_password(int(values['PASSLEN']))
            password_manager.add_password(service_name, cryptography_management.encryption(generated_password))
            ok_window()
    window.close()


