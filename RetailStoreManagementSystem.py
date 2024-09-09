from signal import raise_signal
from matplotlib.colors import to_rgba_array
import inspect

class Store:
    grocery = {
    'rice': {'cost': 40.0, 'quantity': 5},
    'wheat flour': {'cost': 30.0, 'quantity': 2},
    'sugar': {'cost': 20.0, 'quantity': 3},
    'oil': {'cost': 100.0, 'quantity': 1},
    'salt': {'cost': 10.0, 'quantity': 2},
    'spices': {'cost': 50.0, 'quantity': 1},
    'tea': {'cost': 35.0, 'quantity': 2}
    }


    milkproducts = {
    'milk': {'cost': 30.0, 'quantity': 2},
    'yogurt': {'cost': 20.0, 'quantity': 5},
    'cheese': {'cost': 50.0, 'quantity': 1},
    'butter': {'cost': 35.0, 'quantity': 3},
    'cream': {'cost': 25.0, 'quantity': 2},
    'cottage cheese': {'cost': 45.0, 'quantity': 1},
    'sour cream': {'cost': 30.0, 'quantity': 2}
    }


    snacks = {
    'chips': {'cost': 20.0, 'quantity': 10},
    'cookies': {'cost': 30.0, 'quantity': 15},
    'crackers': {'cost': 25.0, 'quantity': 8},
    'candy': {'cost': 5.0, 'quantity': 20},
    'popcorn': {'cost': 15.0, 'quantity': 5},
    'nuts': {'cost': 50.0, 'quantity': 12},
    'chocolate': {'cost': 40.0, 'quantity': 7}
    }




    items  = {

    
        "Grosery" : grocery, 
        "Milkitems":milkproducts, 
        "Snacks" : snacks
    }

    
        
    total = 0 
    total_Given_list_of_items = set()
    that_much_not_avail = set()
    not_in_stock = set()
    def Buy(self,item,quantity):
        total_items  = [] 
        total_price= [] 
        total_quantity = []
        qn = False 
        Pd = False
        for cate in list(Store.items.values()) : 
            for items_of_cate in cate.keys() : 
                # print(items_of_cate)
                if item == items_of_cate  : 
                    # print(cate.get(items_of_cate)["quantity"] )
                    if quantity <= cate.get(items_of_cate)["quantity"] :
                        cate.get(items_of_cate)["quantity"] = cate.get(items_of_cate)["quantity"] - quantity 
                        price = cate.get(items_of_cate)["cost"]
                        Store.total = Store.total + price*quantity 
                        total_items.append(item)
                        total_price.append(price*quantity)
                        total_quantity.append(quantity)
                        Store.total_Given_list_of_items.add(item)
                        # print("Price   : " + str(price * quantity))
                    
                
        
        Store.Bill(self,total_items,total_quantity,total_price)
       
     
    def ShowStock(self):
        # print(list(list(Store.items.values())[1].values())[1]['quantity'])
        for i , v in list(Store.items.items()): 
            print()
            print("="*80)
            print("     "*10 + i)
            print("Product"  + " "*24 + "Quantity" +  " "*8 + "Cost" )
            for items in list(v.items() ):
                
                print(f'{items[0]}',end ="")
                def giveSpc(): 

                    return (32 - len(str(items[0])))*" "
                def giveSpcA(): 
                    return (12-len(str(items[1]["quantity"])))*" "
                print(giveSpc(),end="")
                print(f'{items[1]["quantity"]}',end="   ")
                print(giveSpcA(),end="")
                print(f'{items[1]["cost"]}₹')
        
    def ArrangeByQn(self) :  
        print("Quantity wise Arranged")
        def Arranged(): 
            def giveSpcToABQ(x) : 
                return (24-len(str(x)))*" "
            def giveSpc2ToABQ(y) : 
                return (8-len(str(y)))*" "
            for i in nww : 
                print(f"{i[0]}",end="")
                print(giveSpcToABQ(i[0]),end = "")
                print(f'{i[1]["quantity"]}',end="")
                print(giveSpc2ToABQ(i[1]["quantity"]),end="")
                print(f'{i[1]["cost"]}')
        def giveQn(x) : 
            return x[1]["quantity"]
        nw = Store.items.values()
        for i in range(0,3): 
            print("====================================")
            nww = sorted(list(list(nw)[i].items()), key = lambda x : x[1]["quantity"],reverse=True)
            
            Arranged()


    def BuyInBulk(self,lis1,lis2) :
            total_price = 0 
            products = 0  
            for i in range(len(lis1)): 
                Store.Buy(self,lis1[i],lis2[i])
            print("Total Cost of : " + str(Store.total_Given_list_of_items) + " is " + str(Store.total))
            
            print()
            print(f"Not Available product : {set(lis1)-Store.total_Given_list_of_items}")
            print()
            Store.total = 0 
            Store.total_Given_list_of_items = set()
            

    def Bill(self,i,q,p) : 
            
            if i==[] : 
                print("Not Available")
            for k in range(len(i)): 
                print(f"{i[k]}----{q[k]}----{p[k]}")
            # print(f"Not Available product : {set(i)-Store.total_Given_list_of_items}")
            


       
            
        
            


def Main() : 
    while(True)  : 
        customer = Store() 
        customer.ShowStock()
        act =  0 
        try : 
            act = int(input("11 For Buy | 22 for Show Arranged Data Quantity Wise |55 Buy in Bulk | 00 for Leave "))
        except Exception as e  : 
            print("Error : " + str(e))
            print("Enter only Numbers  " )
        
        if act == 11  : 
            try : 
                pr = input("Item : ")
                qn = int(input("Quantity : "))

                print()
                print("...............Bill.................")
            
                customer.Buy(pr,qn)
                print("Total Cost of : " + str(Store.total_Given_list_of_items) + " is " + str(Store.total))
                Store.total = 0 
                Store.total_Given_list_of_items = set()
            except Exception as e : 
                print("Error : " + str(e) )
                print("Enter Item name in string and quantity in numbers " )
                
            
        elif act== 22  : 
            customer.ArrangeByQn() 
        elif act ==  00 : 
            break 
        elif act == 55 : 
            try : 
                pr = eval(input())
                qn = eval(input())
                print()
                print("...............Bill.................")
                customer.BuyInBulk(pr,qn)
                print("....................................")
            except Exception as e : 
                print("Error : " + str(e))
                print("Enter Both values like this " ) 
                print("['milk','cheese']")
                print("[1,3]")
            
            
        else : 
            print("Valid insertion only")


Main()

        

                
            
                


