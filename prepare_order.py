"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
from users import *
from products import *
from util import *
from orders import *

    
class PrepareOrder:
 #Write your code here
 def __init__(self):
        self.file_manager = CSVFileManager()
        self.user_converter = UserConverter()
        self.product_converter = ProductConverter()

        self.cashiers = []
        self.customers = []
        self.products = []

def load_data(self):
# 1. Leer archivos CSV e instanciar CSVFileManager
# 2. Convertir a listas de objetos
        
# Cargar Usuarios
        df_cashiers = self.file_manager.read("data/cashiers.csv")
        self.cashiers = self.user_converter.convert(df_cashiers, "cashier")
        
        df_customers = self.file_manager.read("data/customers.csv")
        self.customers = self.user_converter.convert(df_customers, "customer")

        # Cargar Productos
        df_hamburgers = self.file_manager.read("data/hamburgers.csv")
        self.all_products.extend(self.product_converter.convert(df_hamburgers, "hamburger"))
        
        df_sodas = self.file_manager.read("data/sodas.csv")
        self.all_products.extend(self.product_converter.convert(df_sodas, "soda"))
        
        df_drinks = self.file_manager.read("data/drinks.csv")
        self.all_products.extend(self.product_converter.convert(df_drinks, "drink"))
        
        df_happymeals = self.file_manager.read("data/happyMeal.csv")
        self.all_products.extend(self.product_converter.convert(df_happymeals, "happymeal"))

def find_cashier(self, dni: str):
        for c in self.cashiers:
            if c.dni == dni:
                return c
        return None

def find_customer(self, dni: str):
        for c in self.customers:
            if c.dni == dni:
                return c
        return None

def find_product(self, prod_id: str):
        for p in self.all_products:
            if p.id == prod_id:
                return p
        return None

def show_products(self):
        print("\n--- Catálogo de Productos ---")
        self.product_converter.print_info(self.all_products)
        print("-----------------------------\n")

def run(self):
        self.load_data()
        
        print("=== SISTEMA DE COMIDA RÁPIDA ===")
        
# 3a. Buscar cajero
        c_dni = input("Ingrese el DNI del Cajero: ")
        cashier = self.find_cashier(c_dni)
        if not cashier:
            print("Cajero no encontrado. Abortando...")
            return

# 3b. Buscar cliente
        cust_dni = input("Ingrese el DNI del Cliente: ")
        customer = self.find_customer(cust_dni)
        if not customer:
            print("Cliente no encontrado. Abortando...")
            return

# 3c. Inicializar orden
        order = Order(cashier, customer)

# 3d y 3e. Escoger y agregar productos
        while True:
            self.show_products()
            p_id = input("Ingrese el ID del producto a agregar (o 'Q' para finalizar orden): ")
            if p_id.upper() == 'Q':
                break
            
            product = self.find_product(p_id)
            if product:
                order.add(product) # 3f. Agregar productos
                print(f"¡{product.name} agregado a la orden!")
            else:
                print("ID de producto no válido. Intente nuevamente.")

# 4. Mostrar Orden
        if order.products:
            order.show()
        else:
            print("\nLa orden está vacía. No se generó ticket.")

if __name__ == "__main__":
    app = PrepareOrder()
    app.run()

