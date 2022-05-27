######################## clase cliente 
#@1 .-se resgistra y @2 .- procede a inicar seccion 
# @3 .- luego va a una tienda y deja rastro (registro en una tienda )
# @4 .- Ver el historial de las tiendas que visitó
# @5 .- Ver su estado. Un estado de cliente puede tener 3 valores posibles:
            # 1. posibles: Normal = sin covid
            # 2. Caso,= tiene covid 
            # 3. Cercano = de 11am  a 1pm son cercano  -------------------condicion por defful ----------------

######################## clase tienda
# @1 .- Un estado de tienda puede tener 2 valores posibles:     ( Normal, Caso.)

######################## clase administrador 
#  @1 .- Ver los detalles de todos los clientes,   [  Nro. Nombre Teléfono Estado]
        #  los detalles de todas las tiendas,      [  Nro. Nombre Teléfono Gerente Estado]
        #  el historial de visitas.                [  Nro. Fecha Hora Cliente Tienda]

#  @2 .- si hay caso (tienda en caso true, personas (cercanos))
#=====================================================================================
from datetime import datetime
#  _______________________________________________________________________________________________ 
## CLASE TIENDA  __________________________________________________________________________________
#  _______________________________________________________________________________________________ 
class Tienda:
    def __init__(self, nomTienda,estadoTienda, gerente):
        self.atrib1 = nomTienda
        self.atrib2 = int(estadoTienda) # @1
        self.atrib3 = gerente
# ______________________________________________________________________________________________
## CLASE CLIENTE _________________________________________________________________________________
# _______________________________________________________________________________________________ 
class Cliente():
    def __init__(self, nom, telef, estado):
        '''aqui se  tiene el costructor
            hay un atributo de tipo int'''
        self.atributo1 = nom 
        self.atributo2 = telef
        self.atributo3 = int(estado)

    
    def RegistCuenta(self, nombre, telefon ):# @1
        ''' registra una cuenta para entrar a al sistema o la opcion en la que el cliete podra hacer cosas
               pasa el nombre y telefono del usuario 
               manda usuario y telefono '''
        nombre= input('ingrese nombre: ')
        telefon = input('ingrese # telefono: ')
        self.usuario = nombre + '123'
        print(f' su usuario es {self.usuario}, con num telefono {telefon}')

    def IniciarSeccion(self, usuario): # @2
        '''inicia sessionen el sistema para obtener otras obiones
                manda el permiso para segir en el programa'''
        while True:
            self.usuarioRes = input('ingrese un usario para ingresar: ')
            if self.usuarioRes==usuario:
                print('un saludo para usted.....')
                break
                
    def RegistrarseTienda(self, tienda): # @3  
        '''sirve para registrarse en una tienda
                tienes variables como dia y hora
                recibe del nombre de la tienda
                imprime tienda y dia
            '''
        self.entrarTienda = input('ingrese la tienda que desea ingresar:  ')
       # self.ano = int(input('ingrese año: '))
       # self.mes = int(input(' mes: '))
        self.dia = input(' fecha-> formato[año:mes:dia]: ')
        self.hora = input('hora -> formato[hora:min] : ')
       # self.min = int(input('ingrese minutos: '))
       # self.dia = datetime.strptime(input('ingrese fecha: '))
        if self.entrarTienda == tienda:
            print(f'registrado enla tienda {tienda}, en la fecha [{self.dia}] ')
        else:
            print('no se registro...')
            
    def HistoryTiendaVisita(self, fecha, hora, tienda):# @4    Nro. Fecha Hora Tienda
        ## hacerlo con ficheros 
        ''' este es el historial 
            muestra el historial del cliente'''
        print(f'================\nhistorial;\nfecha: {fecha},\nhora {hora},\ntienda {tienda} ')

    def VerEstado(self, nombre, telefono, estado): # @5   ver estado de covid 
        ''' ve el estado del cliente 
                opcion solo para el cliente 
                '''
        print(f'nonbre: {nombre}, numero de telefono: {telefono}\nusted consta con estado:\n')
        if estado ==1:
            print('1. Normal = sin covid\n')
        if estado ==2:
            print('2. Caso = tiene covid\n')
        if estado ==3:
            print('3. Cercano = de 11am  a 1pm son cercano\n')

#  _______________________________________________________________________________________________ 
### CLASE ADMINISTRADOR __________________________________________________________________________
#  _______________________________________________________________________________________________  
class Admin():
    
    def verDatosClientes(self,funcionEstado):   #  @1.1.     Nro. Nombre Teléfono Estado 
        ''' repeticion de otra funcion que pertenese a otra clase +
                este caso de la clase superclase Cliente
                '''  
        funcionEstado()
    
    def VerEstadoTinda(self, nombreTienda,telefonoTienda, estadoTienda): #@1.2. Nro. Nombre Teléfono Gerente Estado
        ''' en este ve  el estado de la tienda 
                 opcion particular de el administrador
                 '''

        print(f'nonbre Tienda: {nombreTienda}, numero de telefono: {telefonoTienda}\n estado:')
        if estadoTienda ==1:
            print('1. Normal \n')
        if estadoTienda ==2:
            print('2. Caso = \n')
        
    def cambiarEstadoCliente(self, nombre): # @2
        ''' hace cambios el estado delcliente 
         1. posibles: Normal = sin covid
         2. Caso,= tiene covid 
         3. Cercano = de 11am  a 1pm son cercano  -------------------condicion por defful ----------------
        '''
        self.estadoCliente = input(f'actualizar estado dela persona {nombre}; si o no  ')
        if self.estadoCliente == 'si':
             self.atributo3 = 3
        
    def cabiarEstadoTienda(self, nombre, estadoCliente, estadoTienda1):
        self.estadoTienda = input(f'actualizar estado dela persona {nombre}; si o no  ')
        if self.estadoTienda == 'si':
            if estadoCliente == 3 :
                estadoTienda1 ==2
#  _______________________________________________________________________________________________
# print del menu 1 _______________________________________________________________________________
def Op1():
    #menu 1
    '''impresion del menu principal del programa 
    '''
    print('\n------- eliga opcion ----------')
    print('op 1: opciones del cliente')
    print('op 2: opciones del administrador.')
    print('op 3: salir.')
#  _______________________________________________________________________________________________
# print del menu 2  ______________________________________________________________________________
def Op2():
    '''impresion del menu 2 del cliente
    '''
    print('===========')
    print('......opciones del cliente......')
    print('op1: registro al sistema.')
    print('op2: inicie secion')
    print('opc3: menu principal\n')
#  _______________________________________________________________________________________________ 
### menu principal  ______________________________________________________________________________
if __name__ == '__main__':   ## parte incompleta 
    ''' funcion principal del programa donde se maneja la interactividad con todas
     las clases y funciones y procedimientos 
     '''
    ####### lista de para clientes
    listaCliente = list()
    #  por aqui estuvieron los arreglos

    # objetos o instancias creadas estaticamente 
    usuario1= Cliente('',0,False)
    tiendita= Tienda('mary', 1, 'marco')
    administrador = Admin()
    while True:
        #menu 1
        Op1()
        opMenu = int(input('la opcion es? : '))
        # # opcion 1 _______________________________________________________________________________________________ 
        # parte del cliente 
        if opMenu==1:
            ##menu 2
            while True:
                Op2()
                opCliente = int(input('ingrese la opcion.: '))
                # # opcion 1.1. _______________________________________________________________________________________________ 
                if opCliente==1:       ## parte uno del usuario 
                    usuario1.RegistCuenta(usuario1.atributo1, usuario1.atributo2)
                    listaCliente.append(usuario1)
                # # opciojcn 1.2. _______________________________________________________________________________________________ 
                elif opCliente==2:
                     ## parte 2 del codigo 
                    ##### aqui se pressentara el reto del las obciones para el cliente
                    usuario1.IniciarSeccion(usuario1.usuario)
                    while True:
                        opcion= int(input('ingrese opcion\n 1. registrarse en la tienda.\n 2. ver historial de visitas\n 3. ver estado.\n 4. salir.\n > '))
                        #  _______________________________________________________________________________________________
                        #   registrarse en la tienda
                        if opcion == 1:
                            usuario1.RegistrarseTienda(tiendita.atrib1)
                        #  _______________________________________________________________________________________________
                        #  ver historial de visitas
                        if opcion == 2:
                            usuario1.HistoryTiendaVisita(usuario1.dia, usuario1.hora, tiendita.atrib1)
                        #  _______________________________________________________________________________________________ 
                        # ver estado.
                        if opcion ==3:
                            usuario1.VerEstado(usuario1.atributo1, usuario1.atributo2, usuario1.atributo3)
                        #  _______________________________________________________________________________________________ 
                        # 4. salir.  
                        if opcion == 4:
                            print('salir... ')
                        if opcion== 4:
                            break
                elif opCliente == 3:     
                    print('saliendo al menu principal...')
                else :
                    print('error de opcion ')
                if opCliente == 3:
                    break

        # # opcion 2 _______________________________________________________________________________________________ 
        # administrador  (no esta completo por ahora ) ### aqui van los metodos de el admin 
        elif opMenu==2:
            print('==========')
            
        # # opcion 3 _______________________________________________________________________________________________
        # parte para salir  
        elif opMenu==3:
            print('usted salio mi pana ;) ')
        else:

            print('error ;)')
        if opMenu ==3: ## condicion para salir del bucle while 
            break
        
