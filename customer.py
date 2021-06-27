import sys
import pickle
import os
from datetime import datetime,timedelta

import cart_order
import product
#from cart_order import *
#from product import *
"""Class- Customer
Properties: Cust_Id
            Cust_Name
            Cust_Addr
            Cust_PhnNo          
            Cust_UserId            #for login
            Cust_Password          #for login
Method: BuyProducts()          //TODO: Access to all products
        ViewProducts()
        MakePayment()          //TODO: Payment Details Store?
        AddToCart()            
        DeleteFromCart()
Additional
Properties:                    
//Cart List
//Previous Order List
"""
customer_list=[]
product_list=[]

class Customer():

    def __init__(self,Cust_Name,Cust_Addr,Cust_PhnNo,Cust_UserId,Cust_Password):
        self.Cust_Id=id(self)
        self.Cust_Name=Cust_Name
        self.Cust_Addr=Cust_Addr
        self.Cust_PhnNo=Cust_PhnNo
        self.Cust_UserId=Cust_UserId
        self.Cust_Password=Cust_Password
        self.Cart_obj=cart_order.Cart()
        self.Orders_list=[]       #When order made - push object of Order into list

    def add_customer(self):
        global customer_list
        load_custs()

        #for cust in customer_list:
        #    customer_list.append(cust)
        customer_list.append(self)
        if os.path.exists("customer.pickle"):
            with open("customer.pickle","w") as write_fp:
                pickle.dump(customer_list,write_fp)
                #pickle.dump(Product.product_list,__db_Pointer) 
        else:
            print("Pickle file 'customer.pickle' not found")
     

    def view_products():
        print("Products in Store")
        print("-----------------------")
        product.display_Prods()

    def add_to_cart(self,prod):
        self.Cart_obj.add_prod_to_cart(prod)
        dump_custs()
        print("Product Added to Cart")

    def remove_from_cart(self,prod):
        self.Cart_obj.del_prod_from_cart(prod)
        dump_custs()
        print("Product Removed from Cart")   

    def empty_cart(self):                          #display this option in menu???
        cart_order.empty_cart(self.Cart_obj)
        print("Cart is Empty")
        
    def place_order(self):
        print("Order Details")
        print("---------------------")
        self.Cart_obj.diplay_cart()
        print("---------------------")
        print("1.Place Order")
        print("2.Back/Menu Menu")
        print("3.Exit")
        choice=int(input("Choose option: "))
        while (choice > 3 or choice <1):
            choice=int(input("Please Enter Valid Option : "))
        if (choice == 3):
            sys.exit()
        elif( choice == 1):
            opt=self.make_payment()
            #Set Order Date , Delivery Date
            #Copy Cart items to order obj and push to list
            orderdate=datetime.now().date()
            deldatetime=datetime.now()+timedelta(days=2)
            deldate=deldatetime.date()
            order=cart_order.Order()
            for prod in self.Cart_obj.Cart_product_list:
                order.Order_product_list.append(prod)
            self.Cart_obj.empty_cart()
            order.Order_total_price=self.Cart_obj.Cart_total_price
            order.Order_date=orderdate
            order.Order_deli_date=deldate
            self.Orders_list.append(order)
            dump_custs()
            print("Your Order has been Placed Successfully !")
            print("Your Order will be received on "+str(deldate))   
        #elif (choice == 2):
            #done Automatically


    def make_payment(self):    #TODO :Store card details
        print("Choose Payment Option")
        print("---------------------")
        print("1.Cash On Delivery")
        print("2.Credit / Debit Card")
        print("3.Back/Menu Menu")
        print("4.Exit")
        choice=int(input("Choose option: "))
        while (choice > 4 or choice <1):
            choice=int(input("Please Enter Valid Option : "))
        if (choice == 4):
            sys.exit()
        elif( choice == 1):
            print("You need to pay "+str(self.Cart_obj.Cart_total_price)+"rs during Delivery")
        elif(choice == 2):
            card_no=raw_input("Enter Card Number : ")
            card_name=raw_input("Enter Card Name : ")
            cvv=raw_input("Enter CVV : ")
            print("Transaction Successful")


def load_custs():
    global customer_list
    out_list=[]
    if os.path.exists("customer.pickle"):
        read_fp=open("customer.pickle","r")
        out_list=pickle.load(read_fp)
        customer_list=out_list
        read_fp.close()
    else:
        print("Database File not Found- the system may not function properly ")


def dump_custs():
    if os.path.exists("customer.pickle"):
            write_fp = open("customer.pickle","w")
            pickle.dump(customer_list,write_fp)
            write_fp.close()
    else:
         print("Pickle file 'customer.pickle' not found")



def display_customers():
    print("Customer Details")
    print("  CutomerId  CustomerName  Address  Phoneno  CartDetails  PreviousOrders")
    print("--------------------------------------------------------------------------")
    i=0
    if(customer_list!= None):
        for cust in customer_list:
            print(str(i)+"  "+str(cust.Cust_Id)+"  "+cust.Cust_Name)
            print("   "+cust.Cust_Addr+"  "+str(cust.Cust_PhnNo))
            if(len(cust.Cart_obj.Cart_product_list) != 0):
                print("Total Cart Price : "+str(cust.Cart_obj.Cart_total_price))
                for prod in cust.Cart_obj.Cart_product_list:
                    print(str(prod.Prod_Id)+"  "+prod.Prod_Name+"  "+str(prod.Prod_Price))
            if(len(cust.Orders_list) != 0):
                for order in cust.Orders_list:  #Not displaying each prod in order
                    print(str(order.Order_date)+"  "+str(order.Order_total_price))
            i=i+1


def login(userid,pswd):
    global customer_list
    flag=0
    load_custs()
    if(customer_list!= None):
        for cust in customer_list:
            if(cust.Cust_UserId == userid and cust.Cust_Password == pswd):
                flag=1
                menu(cust)
                break;
    if(flag== 0):
        print("Login Failed ! Try Again")



#Customer obj
def menu(Cust): 
    print("Logged in as '"+Cust.Cust_Name+"'")
    global customer_list
    global product_list 
    customer_list=load_custs()
    product_list=product.load_prods()
    choice=1
    while( choice != 7):
        print("Menu")
        print("---------------------")
        print("1.View Products")
        print("2.Add Product to Cart")
        print("3.Delete Product from Cart")
        print("4.View Cart")
        print("5.Place Order")
        print("6.View Previous Orders")
        print("7.Back/Main Menu")
        print("8.Exit")
        choice=int(raw_input("Choose option: "))
        while (choice > 8 or choice <1):
            choice=int(raw_input("Please Enter Valid Option : "))
        if (choice == 8):
            sys.exit()
        elif( choice == 7):
            return;                 #TODO:Check if goes back
        elif( choice == 1):
            product.menu()
            
        elif( choice == 2):
            prod_name=raw_input("Enter Product Name to add to Cart : ")
            print("-----------------------------------------")
            prod=product.get_ProdByName(prod_name)
            if(prod != None):
                Cust.add_to_cart(prod)
        elif(choice == 3):
            prod_name=raw_input("Enter Product Name to remove from Cart : ")
            print("-----------------------------------------")
            prod=product.get_ProdByName(prod_name)
            if(prod != None):
                Cust.remove_from_cart(prod)
        elif(choice == 4):
            print("Items in Cart")
            print("-------------------------")
            Cust.Cart_obj.diplay_cart()
        elif(choice == 5):
            Cust.place_order()
        elif(choice == 6):
            if(len(Cust.Orders_list) != 0):
                for order in cust.Orders_list:  
                    print(str(order.Order_date)+"  "+str(order.Order_total_price))
                    for prod in order.Order_product_list:
                        print("     "+prod.Prod_Name+"  "+str(prod.Prod_Price))
            else:
                print("You have no Previous Orders")
