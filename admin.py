import sys
import os
import pickle

import product
import customer

"""
Only one username and password for admin
UserId - admin
Password - admin123

Class- Customer
Properties: Adm_Id
            Adm_Name
Method: AddProducts()
        DeleteProducts()
        ViewProducts()
        ViewCustomers()            
"""
customer_list=[]
product_list=[]

class Admin():

    def __init__(self,Adm_Name):
        self.Cust_Id=id(self)
        self.Adm_Name=Adm_Name
    
    def add_Product(self):
        print("Enter Product Details")
        prod_name=raw_input("Enter Product Name : ")
        prod_grp=raw_input("Enter Product Group : ")
        prod_subgrp=raw_input("Enter Product Sub Group : ")
        prod_price=raw_input("Enter Product Price : ")
        prod=product.Product(prod_name,prod_grp,prod_subgrp,prod_price)
        product.add_new_product(prod)
        print("Product Added Susscessfully")

    def delete_Product(self):
        prod_name=raw_input("Enter Product Name to delete : ")
        product.delete_product(prod_name)


    def view_Customers(self):
        customer.display_customers()



def login(username,pswd):
    if(username == 'admin' and pswd=='admin123'):
        print("Admin Login Successfull")
        adm_obj=Admin('admin')
        menu(adm_obj)
    else:
        print("Admin Login Failed")


def menu(admin):
    print("'Admin' Logged in")
    global customer_list
    global product_list 
    customer_list=customer.load_custs()
    product_list=product.load_prods()
    choice=1
    while( choice != 5):
        print("Menu")
        print("---------------------")
        print("1.View Products")
        print("2.Add Product to Store")
        print("3.Delete Product from Store")
        print("4.View Customers")
        print("5.Back/Main Menu")
        print("6.Exit")
        choice=int(raw_input("Choose option: "))
        while (choice > 6 or choice <1):
            choice=int(raw_input("Please Enter Valid Option : "))
        if (choice == 6):
            sys.exit()
        elif( choice == 5):
            return;                 #TODO:Check if goes back
        elif( choice == 1):
            product.menu()
        elif( choice == 2):
            admin.add_Product()
        elif( choice == 3):
            admin.delete_Product()
        elif( choice == 4):
            admin.view_Customers()

