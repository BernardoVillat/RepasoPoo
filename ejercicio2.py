# Definir una excepción personalizada para manejar problemas relacionados con la cuenta de usuario
class CuentaUsuarioException(Exception):
    pass

# Definir la clase CuentaUsuario
class CuentaUsuario:
    def __init__(self, usuario, saldo_inicial=0):
        self.usuario = usuario
        if saldo_inicial < 0:
            raise CuentaUsuarioException("El saldo inicial no puede ser negativo.")
        self.saldo = saldo_inicial
        print(f"El saldo inicial es: {self.saldo}")

    def depositar(self, cantidad):
            if cantidad <= 0:
                raise CuentaUsuarioException("La cantidad a depositar debe ser mayor que cero.")
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${cuenta.consultar_saldo()}")


    def retirar(self, cantidad):
            if cantidad <= 0:
                raise CuentaUsuarioException("La cantidad a retirar debe ser mayor que cero.")
            elif cantidad > self.saldo:
                raise CuentaUsuarioException("Saldo insuficiente para realizar la operación.")
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${cuenta.consultar_saldo()}")



    def consultar_saldo(self):
        return self.saldo

# Ejemplo de uso
if __name__ == '__main__':
        cuenta = CuentaUsuario("Bernardo", 1000)
        while True:
            opcion = input("Menú: \n 1- Hacer un depósito \n 2- Hacer un retiro \n 3- Salir \n Opción: ")
            if opcion == '1':
                try:
                    cantidad_a_depositar = int(input("¿Que cantidad desea depositar? "))
                    resultado_deposito = cuenta.depositar(cantidad_a_depositar)
                except CuentaUsuarioException as cue:
                    print(f"Error en la cuenta de {cuenta}: {cue} ")
            elif opcion == '2':
                try:
                    cantidad_a_retirar = int(input("¿Qué cantidad desea retirar? "))
                    resultado_retiro = cuenta.retirar(cantidad_a_retirar)
                except CuentaUsuarioException as cue:
                    print("Error en la cuenta de usuario: ", cue)
            elif opcion == '3':
                break
            else:
                print("Escoja una opción válida")




