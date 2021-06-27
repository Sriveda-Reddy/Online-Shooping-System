import pickle
import os
import sys

"""
Class-Product
Properties:Prod_Id
           Prod_Name
           Prod_Group
           Prod_SubGroup
           Prod_Price
"""
product_list=[]

class Product():

    def __init__(self,Prod_Name,Prod_Group,Prod_SubGroup,Prod_Price):
        self.Prod_Id=id(self)
        self.Prod_Name=Prod_Name
        self.Prod_Group=Prod_Group
        self.Prod_SubGroup=Prod_SubGroup
        self.Prod_Price=Prod_Price
        

def add_new_product(prod):
    global product_list
    if(product_list!=None):
        product_list.append(prod)
        if os.path.exists("product.pickle"):
            with open("product.pickle","w") as write_fp:
                pickle.dump(product_list,write_fp)
                #pickle.dump(Product.product_list,__db_Pointer) 
        else:
            print("Pickle file 'product.pickle' not found")


def delete_product(prod_name):
    global product_list
    if(product_list!=None):
        for prod in product_list:
            if(prod.Prod_Name == prod_name):
                product_list.remove(prod)
    #Update Pickle
    if os.path.exists("product.pickle"):
        with open("product.pickle","w") as write_fp:
            pickle.dump(product_list,write_fp)
            #pickle.dump(Product.product_list,__db_Pointer)
    else:
        print("Pickle file 'product.pickle' not found")


def load_prods():
    global product_list
    out_list=[]
    if os.path.exists("product.pickle"):
        pickle_in=open("product.pickle","r")
        out_list=pickle.load(pickle_in)
        product_list=out_list
        pickle_in.close()
        return product_list
    else:
        print("Database File not Found- the system may not function properly ")
        return None
    #Product.__db_readptr=Product_DBObj.getInstance()

    
def display_Prods():
    #From Data Structure
    global product_list
    print("Products in Store")
    print("   ProductId   ProductName    Category: Group - SubGroup   Price")
    print("----------------------------------------------------------------------")
    i=1
    if(product_list!=None):
        for prod in product_list:
            print(str(i)+" "+str(prod.Prod_Id)+"  "+prod.Prod_Name+"  "+prod.Prod_Group+" - "+prod.Prod_SubGroup+"    "+str(prod.Prod_Price))
            i=i+1
    #From Pickle
    """
    ouput_list=[]
    pickle_in=open("products.pickle","r")
    output_list=pickle.load(pickle_in)
    i=1
    for prod in output_list:
        print(str(i)+" "+str(prod.Prod_Id)+"  "+prod.Prod_Name+"  "+prod.Prod_Group+" "+prod.Prod_SubGroup+" "+str(prod.Prod_Price))
        i=i+1
    pickle_in.close()
    """


def search_ProdByName(prod_name):
    global product_list
    flag=0
    print("   ProductId   ProductName    Category: Group - SubGroup   Price")
    print("----------------------------------------------------------------------")
    if(product_list!=None):
        for prod in product_list:
            if(prod.Prod_Name == prod_name):
                flag=1
                print(str(prod.Prod_Id)+"  "+prod.Prod_Name+"  "+prod.Prod_Group+" - "+prod.Prod_SubGroup+"    "+str(prod.Prod_Price))
        if(flag == 0):
            print("Sorry ! Product is not present")



def get_ProdByName(prod_name):
    flag=0
    if(product_list!=None):
        for prod in product_list:
            if(prod.Prod_Name == prod_name):
                flag=1
                #print("   ProductId   ProductName    Category: Group - SubGroup   Price")
                #print("----------------------------------------------------------------------")
                #print(str(prod.Prod_Id)+"  "+prod.Prod_Name+"  "+prod.Prod_Group+" - "+prod.Prod_SubGroup+"    "+str(prod.Prod_Price))
                return prod
    if(flag == 0):
        print("Sorry ! Product is not present")
        return None


def search_ProdByCategory(prod_group):
    global product_list
    flag=0
    print("   ProductId   ProductName    Category: Group - SubGroup   Price")
    print("----------------------------------------------------------------------")
    if(product_list!=None):
        for prod in product_list:
            if(prod.Prod_Group == prod_group):
                flag=1
                print(str(prod.Prod_Id)+"  "+prod.Prod_Name+"  "+prod.Prod_Group+" - "+prod.Prod_SubGroup+"    "+str(prod.Prod_Price))
    if(flag == 0):
        print("Sorry ! No Products in given Category")


def menu():
    global product_list
    product_list=load_prods()
    choice=1
    while( choice != 4):
        print("Menu")
        print("---------------------")
        print("1.View All Products")
        print("2.Search Product By Name")
        print("3.Search Product By Category")
        print("4.Back/Main Menu")
        print("5.Exit")
        choice=int(raw_input("Choose option: "))
        while (choice > 5 or choice <1):
            choice=int(raw_input("Please Enter Valid Option : "))
        if (choice == 5):
            sys.exit()
        elif( choice == 4):
            return;                 #TODO:Check if goes back
        elif( choice == 1):
            display_Prods()
        elif( choice == 2):
            prod_name=raw_input("Enter Product Name to Search : ")
            print("-----------------------------------------")
            search_ProdByName(prod_name)
        elif( choice == 3):
            prod_group=raw_input("Enter Product Category to Search : ")
            print("-----------------------------------------")
            search_ProdByCategory(prod_group)




#Not Using
class Product_DBObj:
    __read_fp=None

    def __init__(self):
        """ Virtually private constructor. """
        if Product_DBObj.__read_fp != None:
            raise Exception("This class is a singleton!")
        else:
            if os.path.exists("product.pickle"):
                Product_DBObj.__read_fp = open("product.pickle","r")
            else:
                print("Database File not Found- the system may not function properly ")
                write_fp = open("product.pickle","w")
                write_fp.close()
                Product_DBObj.__read_fp = open("product.pickle","r")


    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Product_DBObj.__read_fp == None:
            Product_DBObj()
        return Product_DBObj.__read_fp