# A shopping cart written in oop
class ShoppingCart(object):
    def __init__(self):
        self.total=0
        self.item={}
       
   #Add item to cart
    def add_item(self,item_name,quantity,price):
         self.item_name=item_name
         self.price=price
         self.quantity=quantity
      
         if self.item_name in self.item:
             #Check if item name is already in cart, if it is add to the quantity

             self.item[self.item_name]= self.item[self.item_name]+self.quantity
      
         else:
             #Else go ahead and add it new
             self.item[self.item_name]=self.quantity
         #return total    
         self.total=self.total+(self.quantity*self.price)
         return (self.total,self.item)
    
    #Remove item from cart    
    def remove_item(self, item_name, quantity, price):
         self.item_name = item_name
         self.quantity_1 = quantity
         self.price = price
         if self.quantity_1 > self.quantity:
             self.total=self.total-(self.quantity*self.price)
             self.item={self.item_name:quantity}
           
         else:
             self.total = self.total - (self.quantity_1 * self.price)
             self.new_item_quantity = self.item[self.item_name] - self.quantity_1
             self.item[self.item_name] = self.new_item_quantity
           
         return (self.total, self.item)



 