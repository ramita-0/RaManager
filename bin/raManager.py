import pickle
from getpass import getpass
from os import system
from hashlib import sha256
cls = lambda: system('cls')
cls()

#Falta implementar seguridad con sha256 para no poder leer ni las cuentas, ni el login maestro al abrir el pkl desde los archivos
#El problema es que si lo implemento, aunque se encripte, si alguna persona decide borrar el archivo "master.pkl", el programa va a generar un nuevo archivo vacio, pidiendo un nuevo login
#Entonces la persona ingresa un login aleatorio, y puede acceder a todas las cuentas de "data.pkl", la solucion seria que cuando el "master.pkl" esta vacio, tambien a su vez generar un nuevo
#"data.pkl"
def getLoginData():
    loginData = {}

    with open("master.pkl", "rb") as file:
        while True:
            try:
                login = pickle.load(file)
                loginData.update(login)

            except EOFError:
                break

    return(loginData)

def login():
    login = getLoginData()

    if len(login) == 0:
        newLogin = {}

        print("---- Bienvenido al registro del sistema de control de contraseñas! ----")
        print("\nIngrese un nombre de usuario:")
        newUser = input("-> ")

        print("\nIngrese una contraseña maestra, esta sera utilizada para acceder a sus datos, asi que no la olvide!")
        newPass = getpass("-> ")

        print("\nConfirme su contraseña:")
        newPass2 = getpass("-> ")

        while True:
            if newPass != newPass2:
                cls()
                print("---- Bienvenido al registro del sistema de control de contraseñas! ----")
                print("\nLas contraseñas no coinciden, intentelo denuevo")
                newPass = getpass("-> ")
                
                print("\nConfirme su contraseña:")
                newPass2 = getpass("-> ")

            else:
                cls()
                printMenu()
                break

        newLogin[newUser] = newPass

        file = open("master.pkl", "ab")
        pickle.dump(newLogin, file)
        file.close()
        
    else:
        user = {}
        with open("master.pkl", "rb") as file:
            while True:
                try:
                    userLeido = pickle.load(file)
                    user.update(userLeido)

                except EOFError:
                    break
        
        nombreUser = next(iter(user))
        print("---- Bienvenido/a ", nombreUser, "! ----\n")
        print("Ingrese la contraseña maestra: ")
        
        while True:
            passInput = getpass("-> ")

            if passInput == user.get(nombreUser):
                cls()
                printMenu()
                break

            else:
                cls()
                print("---- Bienvenido/a ", nombreUser, "! ----\n")
                print("-Contraseña incorrecta-\n")
                print("Ingrese la contraseña maestra: ")
                
def printMenu():
    print("\n-Input mode-\n")
    print("         view       -ver todas las cuentas almacenadas")
    print("         create     -crear una nueva cuenta")
    print("         delete     -borrar una cuenta")
    print("         edit       -editar una cuenta")
    print("         exit       -salir del programa")
    print("         (enter)    -ir al menu")

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
        print("\nIngrese una contraseña")
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
        print("\nIngrese la nueva contraseña")
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