"""
Class-Cart
Properties:Cart_Id
           Num_of_Prods
           Total
"""

#TODO :Quantity of Prods
class Cart():
	def __init__(self):
		self.Cart_Id=id(self)
		self.Cart_product_list=[]
		self.Cart_total_price=0


    def add_prod_to_cart(self,prod):
    	self.Cart_product_list.append(prod)
    	pri=self.Cart_total_price
    	self.Cart_total_price=pri_prod.Prod_Price


    def del_prod_from_cart(self,prod):
    	if prod in self.Cart_product_list:
    		pri=prod.Prod_Price
    		self.Cart_product_list.remove(prod)
            temp=self.Cart_total_price - pri
            self.Cart_total_price=temp
        else:
        	print("Error:Given Product not present in Cart to Remove")

    def empty_cart(self):
    	self.Cart_product_list=[]
    	self.Cart_total_price=0
