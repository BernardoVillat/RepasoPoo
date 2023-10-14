# Definir excepciones personalizadas
class EstudianteException(Exception):
    pass

# Definir la clase Estudiante
class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise EstudianteException("El nombre no puede estar vacío.")
        self.nombre = nuevo_nombre
        print(f"Nombre actualizado correctamente \nSu nombre ahora es: {self.nombre}")


    def actualizar_apellido(self, nuevo_apellido):
        if not nuevo_apellido:
            raise EstudianteException("El apellido no puede estar vacío.")
        self.apellido = nuevo_apellido
        print(f"Apellido actualizado correctamente \nSu apellido ahora es: {self.apellido}")

    def actualizar_carnet(self, nuevo_carnet):
        if len(nuevo_carnet) != 8 or not nuevo_carnet.isdigit():
            raise EstudianteException("El carnet debe contener exactamente 9 dígitos numéricos.")
        self.carnet = nuevo_carnet
        print(f"Su nuevo carnet es: {self.carnet}")
        
    def actualizar_carrera(self, nueva_carrera):
            if not nueva_carrera:
                raise EstudianteException("El nombre de la carrera no puede estar vacío.")
            self.carrera = nueva_carrera
            print(f"Usted ahora esta estudiando: {self.carrera}")

    def obtener_informacion(self):
        return f"Nombre: {self.nombre} {self.apellido}, Carnet: {self.carnet}, Carrera: {self.carrera}"

if __name__ == '__main__':
    estudiante1 = Estudiante("Bernardo", "Villatoro", "20210012", "Ingeniería Informática")
    while True:
        opcion = input("Menú \n 1- Obtener información del estudiante \n 2- Actualizar nombre del estudiante \n 3- Actualizar apellido del estudiante \n 4- Actualizar carnet \n 5- Actualizar carrera \n 6- Salir \n Opción: ")
        if opcion == '1':
            try:
                print("Información del estudiante:")
                print(estudiante1.obtener_informacion())
            except EstudianteException as e:
                print(f"Error: {e}")
        elif opcion == '2':
            try:
                # Actualizar el nombre del estudiante
                nuevo_nombre = input("Por favor, ingrese el nuevo nombre: ")
                resultado_actualizar_nombre = estudiante1.actualizar_nombre(nuevo_nombre)
            except EstudianteException as e:
                print(f"Error: {e}")
        elif opcion == '3':
            try:
                # Actualizar el apellido del estudiante
                nuevo_apellido = input("Por favor, ingresa el nuevo apellido: ")
                resultado_actualizar_apellido = estudiante1.actualizar_apellido(nuevo_apellido)
            except EstudianteException as e:
                print(f"Error: {e}")
        elif opcion == '4':
            try:
                # Actualizar el carnet del estudiante
                nuevo_carnet = input("Por favor ingresa el nuevo carnet: ")
                resultado_actualizar_carnet = estudiante1.actualizar_carnet(nuevo_carnet)
            except EstudianteException as e:
                print(f"Error: {e}")
        elif opcion == '5':
            try:
                # Actualizar carrera del estudiante
                nueva_carrera = input("Por favor, ingresa tu nueva carrera: ")
                resultado_actualizar_carrera = estudiante1.actualizar_carrera(nueva_carrera)
            except EstudianteException as e:
                print(f"Error: {e}")
        elif opcion == '6':
            break
        else:
            print("Por favor, escoja una opción válida")
            
    print("Información actualizada del estudiante:")
    print(estudiante1.obtener_informacion())
