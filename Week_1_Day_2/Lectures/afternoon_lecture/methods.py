
# building a blueprint so that we can make instances of this blueprint and call methods 
class User:
  def __init__(self, first_name, email, password, favorite_food= "burgers" ):
    #attributes are variables
    self.first_name = first_name
    self.favorite_food = favorite_food
    self.email = email
    self.password = password
    
    
    #create more attributes (maybe add a last name)
    
  def create_attribute(self, number):
    self.age = number
    
    
    #read all the attributes (print all attributes)
    
  def display_info(self):
      print(self.first_name, self.email, self.password)
      
    
    #read one of the attributes (print certain attribute)
    
  def display_name(self):
    print(self.first_name)
    

    
    
    
    def display_favorite_food(self):
      try:
        # (self.favorite_food):
        print(self.favorite_food)
      except:
        print("nothing to display")
        
        
    #update one or more of the attributes (change first name or email
    
  def update_name(self, new_name):
    self.first_name = new_name
    
    
    #delete one or more of the attributes (remove )
    
  def delete_favorite_food(self):
    
    del self.favorite_food
    
Nien = User("Nien", "nien_email@email.com", "12345678")

# Nien.create_attribute(25)

# print(Nien.age)

# Nien.display_info()

# Nien.display_name()

# Nien.update_name("Yuan")

# Nien.display_name()

Nien.display_favorite_food()

Nien.delete_favorite_food()

Nien.display_favorite_food()