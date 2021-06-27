from product import *
from customer import *

prod_list=[]
cust_list=[]

def dump_to_pickle(filename,list):
    with open(filename,'w') as write_fp:
        pickle.dump(list,write_fp)  
    write_fp.close()  


def load_from_pickle(filename):
    with open(filename,'r') as read_fp:
        list=pickle.load(read_fp)
    read_fp.close()
    return list


def main():
    prod_list=[]
    cust_list=[]
    #Adding Products -products.pickle

    p1=Product("Jbl Headphones","Electronics","Mobiles and Accesories", 800)
    prod_list.append(p1)
    p2=Product("NoteBook","Stationary","Book",100)
    prod_list.append(p2)
    p3=Product("Craft Paper","Stationary","Craft",200)
    prod_list.append(p3)
    p4=Product("DreamCatcher","Household","Home Decor",180)
    prod_list.append(p4)
    p5=Product("Women Trendy T-shirt","Fashion","Women",250)
    prod_list.append(p5)
    p6=Product("Women Avaasa Kurti","Fashion","Women",400)
    prod_list.append(p6)
    p7=Product("OnePlus 6","Electronics","Mobiles and Accesories",35000)
    prod_list.append(p7)
    p8=Product("IronBox","Electronics","Home and Kitchen Appliances",600)
    prod_list.append(p8)
    p9=Product("Lenovo Powerbank","Electronics","Mobiles and Accesories",850)
    prod_list.append(p9)
    p10=Product("Honour 8X","Electronics","Mobiles and Accesories",15000)
    prod_list.append(p10)
    p11=Product("Friends Sweatshirt","Fashion","Women",700)
    prod_list.append(p11)
    p12=Product("Men Black Formal Shoe","Fashion","Men",2000)
    prod_list.append(p12)
    p13=Product("Men Jeans","Fashion","Men", 900)
    prod_list.append(p13)
    p14=Product("Women Titan Watch","Fashion","Watches",3500)
    prod_list.append(p14)
    p15=Product("Electric Rice Cooker","Electronics","Home and Kitchen Appliances", 1700)
    prod_list.append(p15)

    dump_to_pickle("product.pickle",prod_list)


    #Adding Customers - customer.pickle
    c1=Customer("John","IIT Hyderabad", 7893951446 , "John" , "john128" )
    cust_list.append(c1)
    c2=Customer("Doe","BITS Pilani", 8297595469 , "Doe" , "doe16" )
    cust_list.append(c2)
    c3=Customer("Xyne","VJIET", 9847243293 , "Xyne" , "xyne168" )
    cust_list.append(c3)
    c4=Customer("Yappy","Kolkata", 9000334345 , "Yappy" , "yapp123" )
    cust_list.append(c4)
    c5=Customer("Zoey","Kukatpally", 9843951484 , "Zoey" , "zoey1234" )
    cust_list.append(c5)

    dump_to_pickle("customer.pickle",cust_list)

    """
    #Printing
    print("Products ")
    print("--------------------------------------------------------------------------------")
    prod_list=load_from_pickle("product.pickle")
    i=1
    for prod in prod_list:
        print(str(i)+"  "+str(prod.Prod_Id)+"  "+prod.Prod_Name+"  "+prod.Prod_Group+"  "+prod.Prod_SubGroup+"  "+str(prod.Prod_Price))
        i=i+1


    print("Customers")
    print("--------------------------------------------------------------------------------")
    cust_list=load_from_pickle("customer.pickle")
    i=1
    for cust in cust_list:
        print(str(i)+"  "+str(cust.Cust_Id)+"  "+cust.Cust_Name+"  "+cust.Cust_Addr+"  "+str(cust.Cust_PhnNo)+"  "+cust.Cust_UserId+"  "+cust.Cust_Password)
        i=i+1
    """



if __name__ == '__main__':
    main()

