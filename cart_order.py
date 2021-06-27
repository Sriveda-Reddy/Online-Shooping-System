"""
Class-Cart
Properties:Num_of_Prods
       Total
"""
#TODO :Quantity of Prods
class Cart():
    def __init__(self):
        self.Cart_product_list=[]
        self.Cart_total_price=0

    def add_prod_to_cart(self,prod):
        self.Cart_product_list.append(prod)
        pri=self.Cart_total_price
        self.Cart_total_price=pri+prod.Prod_Price


    def del_prod_from_cart(self,prod):
        if prod in self.Cart_product_list:
            pri=prod.Prod_Price
            self.Cart_product_list.remove(prod)
            temp=self.Cart_total_price - pri
            self.Cart_total_price=temp
        else:
             print("Error:Given Product not present in Cart to Remove")

    def diplay_cart(self):
        print("Total Cart Price : "+str(self.Cart_total_price))
        i=1
        for prod in self.Cart_product_list:
            print(str(i)+" "+str(prod.Prod_Id)+"  "+prod.Prod_Name+"  "+prod.Prod_Group+" "+prod.Prod_SubGroup+" "+str(prod.Prod_Price))
            i=i+1


    def empty_cart(self):
        self.Cart_product_list=[]
        self.Cart_total_price=0


"""
Class-Order
Properties:prod_list
       Total
       Order Date
       Delivery Date
"""
class Order():

    def __init__(self):
        self.Order_product_list=[]
        self.Order_total_price=0
        self.Order_date="Undefined"
        self.Order_deli_date="Undefined"
  
    #Operations on this done in make_payment or confirm_order
    #Move the products from cart in Order obj and push order obj to Orders_list of Customer
    


