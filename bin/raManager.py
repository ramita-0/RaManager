import pickle
from getpass import getpass
from os import system
from hashlib import sha256
cls = lambda: system('cls')
cls()

#falta implementar primera contrasena maestra para el login

def login():
    pw = ""
    while pw != "test":
        pw = getpass("\nInput master password: ")
        if pw == "test":
            cls()
            break
        else:
            cls()
            print("Incorrect password")

def printMenu():
    print("\n-Input mode-\n")
    print("         view       -view all the accounts that have been created that contain a password")
    print("         create     -create a new account")
    print("         delete     -delete an account")
    print("         edit       -edit an account")
    print("         exit       -exit program")
    print("         (enter)    -go to the menu")

def getAccs():
    cuentasGuardadas = {}
    cuentaActual = {}
    with open("data.pkl", "rb") as file:
            while True:
                try:
                    cuentaActual = pickle.load(file)
                    cuentasGuardadas.update(cuentaActual)
                except EOFError:
                    break
    return(cuentasGuardadas)

def printAccs():
    print("\n-Cuentas registradas-\n")
    for key in getAccs():
        print("         " + key)

def printAccPassword():
    cls()
    printAccs()
    print("\nIngrese la cuenta que quiera ver")
    cuenta = input("-> ")

    if getAccs().get(cuenta):
        cls()
        print("\n-Datos-\n")
        print("         " + cuenta + "  " + getAccs()[cuenta])

    else:
        cls()
        print("Esa cuenta no existe!")
        printMenu()

def addAcc():
    nuevaCuenta = {}
    cls()
    print("\nIngrese el nombre de su cuenta")
    nombreCuenta = input("-> ")

    if nombreCuenta not in getAccs():
        print("\nIngrese una contrasena")
        passCuenta = input("-> ")
        nuevaCuenta[nombreCuenta] = passCuenta

        with open("data.pkl", "ab") as file:
            pickle.dump(nuevaCuenta, file, protocol=pickle.HIGHEST_PROTOCOL)
            cls()
            print("Registrado con exito!")
            printMenu()

    else:
        cls()
        print("Ya existe una cuenta con ese nombre!")
        printMenu()
    
def editAcc():
    cls()
    print("\nIngrese el nombre de la cuenta que quiera editar")
    nombreCuenta = input("-> ")

    aux = {}
    file = open("data.pkl", 'rb+')
    file.seek(0,0)

    if nombreCuenta in getAccs():
        print("\nIngrese la nueva contrasena")
        passCuenta = input("-> ")
        cuentaNueva = {}
        cuentaNueva[nombreCuenta] = passCuenta

        while True:
            try:
                cuenta = pickle.load(file)

                if nombreCuenta not in cuenta:
                    aux.update(cuenta)
                else:
                    aux.update(cuentaNueva)
            except EOFError:
                file.close()
                break

        file = open("data.pkl", "wb")

        for keyActual  in aux:
            valorActual = aux[keyActual]

            dictAux = {}
            dictAux[keyActual] = valorActual
            pickle.dump(dictAux, file)

        file.close()
        cls()
        print("Cuenta editada con exito!")
        printMenu()

    else:
        cls()
        print("Esa cuenta no existe!")
        printMenu()
            
def deleteAcc():
    cls()
    print("\nIngrese el nombre de la cuenta que quiera borrar")
    nombreCuenta = input("-> ")

    aux = {}
    file = open("data.pkl", 'rb+')
    file.seek(0,0)
    
    if nombreCuenta in getAccs():
        while True:
            try:
                cuenta = pickle.load(file)

                if nombreCuenta not in cuenta:
                    aux.update(cuenta)
                    
            except EOFError:
                file.close()
                break

        file = open("data.pkl", "wb")

        for keyActual  in aux:
            valorActual = aux[keyActual]

            dictAux = {}
            dictAux[keyActual] = valorActual
            pickle.dump(dictAux, file)

        file.close()
        cls()
        print("Cuenta borrada con exito!")
        printMenu()

    else:
        cls()
        print("Esa cuenta no existe!")
        printMenu()


login()
printMenu()
while True:
    userInput = input("-> ")

    if userInput == "view":
        printAccPassword()

    elif userInput == "create":
        addAcc()

    elif userInput == "delete":
        deleteAcc()

    elif userInput == "edit":
        editAcc()

    elif userInput == "":
        cls()
        printMenu()
        
    elif userInput == "exit":
        break

    else:
        cls()
        print("Opcion invalida!")
        printMenu()