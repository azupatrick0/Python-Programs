# A shopping cart written in oop
class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.item = {}
       
   #Add item to cart
    def add_item(self,item_name,quantity,price):
         self.item_name = item_name
         self.price = price
         self.quantity = quantity
      
         if self.item_name in self.item:
             #Check if item name is already in cart, if it is add to the quantity
             self.item[self.item_name] += self.quantity
      
         else:
             #Else go ahead and add it new
             self.item[self.item_name] = self.quantity
         #return total    
         self.total += self.quantity * self.price
         return (self.total,self.item)
    
    #Remove item from cart    
    def remove_item(self, item_name, quantity, price):
         self.item_name = item_name
         self.quantity = quantity
         self.price = price

         if self.item_name in self.item:
            if(self.item[self.item_name] >= self.quantity):
                self.item[self.item_name] -= self.quantity
                self.total -= self.quantity * self.price
                return (self.total, self.item)
              
            else:
                print('Item not up to ' + str(self.quantity))