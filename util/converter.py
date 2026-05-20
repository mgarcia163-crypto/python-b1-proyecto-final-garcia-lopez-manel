from abc import ABC, abstractmethod
#Write your code here
import pandas as pd
from products.product import Hamburger, Soda, Drink, HappyMeal
from users.user import Cashier, Customer

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):    
    #Write your code here
      cashiers_list = []
      for _, row in dataFrame.iterrows():
        cajero = Cashier(
          dni=str(row['dni']), 
          name=str(row['name']), 
          age=int(row['age']))
        cashiers_list.append(cajero)
      return cashiers_list

class CustomerConverter(Converter):
  #Write your code here
  def convert(self, dataFrame: pd.DataFrame, *args) -> list:
    customers_list = []
    for _, row in dataFrame.iterrows():
      cliente = Customer(
        dni=str(row['dni']), 
        name=str(row['name']), 
        age=int(row['age']))
      customers_list.append(cliente)
    return customers_list

class ProductConverter(Converter):
  #Write your code here
  def convert(self, dataFrame: pd.DataFrame, *args) -> list:
    products_list = []
        
    if not args:
        raise ValueError("Falta el argumento para identificar el tipo de producto (ej. 'hamburger')")
            
    product_type = str(args[0]).lower()
        
    for _, row in dataFrame.iterrows():
        p_id = str(row['id'])
        p_name = str(row['name'])
        p_price = float(row['price'])
            
        if product_type == "hamburger":
            producto = Hamburger(p_id, p_name, p_price)
        elif product_type == "soda":
            producto = Soda(p_id, p_name, p_price)
        elif product_type == "drink":
            producto = Drink(p_id, p_name, p_price)
        elif product_type == "happymeal":
            producto = HappyMeal(p_id, p_name, p_price)
        else:
            continue
        producto.describe = lambda p=producto: f"[{p.type()}] ID: {p.product_id} - {p.name:<20} | Precio: {p.price:>5.2f}€"
            
        products_list.append(producto)
            
    return products_list