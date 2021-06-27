import cPickle as pickle
import sys

import product
import customer
import admin
import populate
"""
Main File
Displays Menu
"""
def menu():
    #Populating Data inti pickle
    populate.main()
    #Loading  Data Structures
    product.product_list=product.load_prods()
    customer_list=customer.load_custs()

    choice=1
    print("=========== Welcome to Online Shopping System =============")
    while( choice != 5):
        print("Menu")
        print("---------------------")
        print("1.View Products")
        print("2.Login as Admin")
        print("3.Login as Customer")
        print("4.Register as Customer")
        print("5.Exit")
        choice=int(raw_input("Choose option: "))
        while (choice > 5 or choice <1):
            choice=int(raw_input("Please Enter Valid Option : "))
        if (choice == 5):
            sys.exit()
        elif( choice == 1):
            product.menu()
        elif( choice == 2):
            print("Login")
            username=raw_input("Enter User name : ")
            pswd=raw_input("Enter Password : ")
            admin.login(username,pswd)
        elif( choice == 3):
            print("Login")
            username=raw_input("Enter User name : ")
            pswd=raw_input("Enter Password : ")
            customer.login(username,pswd)
        elif( choice == 4):
            print("Enter Your Details")
            cust_userid=raw_input("Enter Customer UserId : ")
            cust_password=raw_input("Enter Customer Password : ")
            cust_name=raw_input("Enter Customer Name : ")
            cust_addr=raw_input("Enter Customer Address : ")
            cust_phnno=raw_input("Enter Customer Phone Number : ")
            cust=customer.Customer(cust_name,cust_addr,cust_phnno,cust_userid,cust_password)
            cust.add_customer()
            print("Registered Successfully")



def main():
    menu()
    

if __name__ == '__main__':
    main()
