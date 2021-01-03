#Por Erlin Zelada
# Al 25 diciembre del 2020


#Importamos las librerías 
import msvcrt
import os
listaClientes = []

#Creamos una clase para realaizar todas las operaciones recursivas 
class Clientes(object):
    def __init__(self, _DNI, _apellidos, _nombres,  _monto, _fecha, _estado, _strike1, _strike2, _strike3):
        self.DNI = _DNI
        self.apellidos = _apellidos
        self.nombres = _nombres
        self.monto = _monto
        self.fecha = _fecha
        self.estado = _estado
        self.strike1 = _strike1
        self.strike2 = _strike2
        self.strike3 = _strike3
        self.StrikeFinal = (_strike1 + _strike2 + _strike3) / 3
        self.historial = []
#Funcion que sera la que imprima los datos, segun se indique
    def imprimirDatos(self):
        print(f"|{ self.DNI:^10}|{self.apellidos:^17}|{self.nombres:^15}|{self.monto:^12}|{self.fecha:^10}|{self.estado:^12}|{self.strike1:^10}|{self.strike2:^10}|{self.strike3:^10}| ")
        
    def nivelactual(self):
        print(f"Hasta el momento su nivel crediticio es de : {self.StrikeFinal} % ")
# Función que nos ayuda a escribir el nivel de puntualidad al pagar
    def nivelPuntualidad(self, _strike1, _strike2, _strike3):
        self.strike1 = _strike1
        self.strike2 = _strike2
        self.strike3 = _strike3
        self.StrikeFinal = (_strike1 + _strike2 + _strike3) / 3
        print(f"El nivel de puntualidad se sitúa en  {self.StrikeFinal}% ")
        
# Función que nos ayuda a escribir el estado del credito
    def editarEstado(self, _estado):
        self.estado = _estado
        print("Actualización Exitosa!")

# Estas funciones nos serviran para mostrar el historial
    def contarAccion(self, _strike1, _strike2, _strike3):
        self.strike1 = _strike1
        self.strike2 = _strike2
        self.strike3 = _strike3
        return (f"Modificacion:\n        Strike_1: {_strike1}\n        Strike_2: {_strike2}\n        Strike_3: {_strike3}\n")

    def contarAccion2(self, _estado):
        self.estado = _estado
        return (f"modificacion:\n        Estado: {_estado} \n")

    def entregaHistorial(self):
        
        print(f"No. DNI: {self.DNI} - {self.apellido} {self.nombres} ")
        
        
        
# Funcion para limpair pantalla
def LimpiarPantalla ():
    os.system("cls")
    
# Funcion para Indicar con una tecla para continuar   
def seguir ():
    print("Presione una tecla para regresar al menú principal")
    msvcrt.getch()
    LimpiarPantalla()

#Funcion del encabezado  
def EncabezadoTabla ():
    print(" ------------------------------------------------------------------------------------------------------------------")
    print("|    DNI   |    APELLIDOS    |    NOMBRES    | MONTO (s/) |   FECHA  |   ESTADO   | STRAKE 1 | STRAKE 2 | STRAKE 3 |")
    print(" ------------------------------------------------------------------------------------------------------------------")
# Funcion de registro del cliente
def registrarCliente():
    print("Registro de Clientes\n")
    EncabezadoTabla()
    DNI = int(input("Ingrese el numero de DNI: "))
    apellidos = input("Ingrese Los APELLIDOS (Ej: ZELADA TAFUR ): ")
    nombres = input("Ingrese los NOMBRES (Ej: ERLIN CECIDIO ): ")
    monto = float(input("Ingrese MONTO en SOLES: (Ejem: 999.99 ): "))
    fecha = input("Ingrese la fecha del Credito (Ej: 01/01/01 ): ")
    estado = input("Ingrese el estado del credito (Ej: ACTIVO/CANCELADO ): ")
    print("---------------------------------------------------------------------------------------------")
    print("NOTA: Los Strake's, Empiezan en 100% y se reducen al orden del 20% por cada día de retraso,  ")
    print("      Existen 3 oportunidades (3 Strake's), los que si; se llega a un promedio menor al 50%; ")
    print("      NO podrá acceder a un proximo credito ------------------------------------------------ ")
    strike1 = int(input("Ingrese Strike 1: "))
    strike2 = int(input("Ingrese Strike 2: "))
    strike3 = int(input("Ingrese Strike 3: "))
    objCliente = Clientes(DNI, apellidos, nombres,  monto, fecha, estado, strike1, strike2, strike3)
    listaClientes.append(objCliente)
    print(" ------------------------------------------------------------------------------------------------------------------")
    LimpiarPantalla()
    print("¡Registro Exitoso!")

#Función para mostrar la lista de clientes

def listadoClientes():
    print("Listado de Clientes\n")
    EncabezadoTabla()
    for objCliente in listaClientes:
        objCliente.imprimirDatos()
    print(" ------------------------------------------------------------------------------------------------------------------")
    seguir()

# Función para Buscar a un cliente
def buscarCliente():
    
    print("Buscar Cliente\n")
    print("")
    DNI = int(input("Ingrese el numero de DNI a buscar: "))
    EncabezadoTabla()
    for objCliente in listaClientes:
        if DNI == objCliente.DNI:
            objCliente.imprimirDatos()
    print(" ------------------------------------------------------------------------------------------------------------------")
    print("")
    
    seguir()

# Función para modificar la puntualidad de pago de un cliente
def modificarPuntualidad():
    
    print("Modificar Puntualidad\n")
    DNI = int(input("Ingrese el numero de DNI del cliente que desea modificar Puntualidad: "))

    for objCliente in listaClientes:
        if DNI == objCliente.DNI:
            print("")
            print("Se actualizará el nivel de puntualidad del siguiente cliente")
            print("")
            EncabezadoTabla()
            objCliente.imprimirDatos()
            print(" ------------------------------------------------------------------------------------------------------------------")
            print("")
            strike1 = float(input("Ingrese Strike 1: "))
            strike2 = float(input("Ingrese Strike 2: "))
            strike3 = float(input("Ingrese Strike 3: "))
            print("")
            indicador = objCliente.contarAccion(strike1, strike2, strike3)
            objCliente.nivelPuntualidad(strike1, strike2, strike3)
            objCliente.historial.append(indicador)
            EncabezadoTabla()
            objCliente.imprimirDatos()
    print(" ------------------------------------------------------------------------------------------------------------------")
    seguir()

#Funcion para modificar el estado del credito, es decir si ya esta cancelado o aun activo
def modificarEstado():
    print("")
    print("Modificar Estado\n")
    DNI = int(input("Ingrese el numero de DNI a del Cliente: "))
    for objCliente in listaClientes:
        if DNI == objCliente.DNI:
            print("")
            print("Se actualizará el estado del credito del siguiente cliente")
            print("")
            EncabezadoTabla()
            objCliente.imprimirDatos()
            print(" ------------------------------------------------------------------------------------------------------------------")
            print("")
            estado = input("Ingrese el estado actual del credito (Activo/Cancelado): ")
            print("")
            objCliente.editarEstado(estado)
            indicador = objCliente.contarAccion2(estado)
            objCliente.historial.append(indicador)
            print("")
            EncabezadoTabla()
            objCliente.imprimirDatos()
    print(" ------------------------------------------------------------------------------------------------------------------")
    seguir()

#Funcion para ver todos los ultimos cambios realizados

def consultarHistorial():
    print("Consulta de Historial\n")
    DNI = int(input("Ingrese el numero de DNI del cliente que desea saber su Historial: "))
    for objCliente in listaClientes:
        if DNI == objCliente.DNI:
            print("Historial de: ")
            for indicador in objCliente.historial:
                print(f"Accion: {indicador}")
            EncabezadoTabla()
            objCliente.imprimirDatos()
            print(" ------------------------------------------------------------------------------------------------------------------")
            objCliente.nivelactual()
        print("")
    
    seguir()
    
#Función para salir del menu principal
def salir():
    print("Salida inminente...!")
    exit()



# Función main Para el menu principal
def main():
    while True:
        print("\n")
        print(" __________________________________________________")
        print("|                                                  |")
        print("|       Creditos EZETA Le da la Bienvenida         |")
        print("|__________________________________________________|")
        print("")
        print("   Menú Principal")
        print("Indique el N° de operación que desea realizar:")
        print("1.- Registrar un Cliente")
        print("2.- Ver lista de Clientes")
        print("3.- Buscar un Cliente")
        print("4.- Modificar Nivel de puntualidad")
        print("5.- Modificar estado del credito")
        print("6.- Consultar Historial crediticio")
        print("7.- Salir\n")

        opcion = int(input("Numero de Operación: "))

        if opcion == 1:
            registrarCliente()
        elif opcion == 2:
            listadoClientes()
        elif opcion == 3:
            buscarCliente()
        elif opcion == 4:
            modificarPuntualidad()
        elif opcion == 5:
            modificarEstado()
        elif opcion == 6:
            consultarHistorial()
        elif opcion == 7:
            salir()

#Hacemos el llamado a la función principal
if __name__ == '__main__':
    main()
