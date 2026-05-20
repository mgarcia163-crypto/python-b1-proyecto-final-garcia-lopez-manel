#Write your code here
from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
  #Write your code here
  def pack(self) -> str:
        return "Food Wrap Paper"
  def material(self) -> str:
        return "Aluminium"

class Bottle(FoodPackage):  
  #Write your code here
  def pack(self) -> str:
        return "Bottle"
        
  def material(self) -> str:
        return "Plastic"
      
class Glass(FoodPackage):  
  #Write your code here
  def pack(self) -> str:
        return "Glass"
        
  def material(self) -> str:
        return "Cardboard"

class Box(FoodPackage):  
  #Write your code here
  def pack(self) -> str:
        return "Box"
        
  def material(self) -> str:
        return "Cardboard"
  