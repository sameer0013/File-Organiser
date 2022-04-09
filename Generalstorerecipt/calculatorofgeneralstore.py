if __name__=='__main__':
    sum=0
    b=[]
    product=[]
    quantity=[]
    count=0
    while(True):
    
        prod=input("\tenter the product: ")
        if product=='q':
            break
        else:
             product.append(str(prod))
        

        qty=input("\tenter the quantity of product:")
        
        if qty=='q':
            break
        else:
            quantity.append(int(qty))
            count=count+int(qty)

        n2=input("\tenter the price: ")
        if n2 !='q':
            
            sum= int(sum)+int(n2)
            b.append(str(n2))
            print("order price is {}".format(sum))

        else:
            break  

    print(f"\nYour total bill is {sum} .\nThanks for coming!")    

    count2=0
    with open("receipt.txt","w") as f:
        f.write("======CENTRAL STORE FOR NECCESSARY PRODUCTS======\n")
        f.write(f"\n\t PRODUCT  :  QUANTITY  :  PRICE ")  
        f.write("\n")      
        for (i,j,k) in zip(product,b,quantity):
            count2=count2+1
            f.write(f"\t{count2}. {i}  :  {k}  :  {j}")        
            f.write("\n")
        f.write("________________________________")    
        f.write(f"\n\tTOTALBILL  :  {sum}  :  {count}")   
        f.write("\n\n======THANKS FOR SHOPPING======")  


    with open("receipt.txt","r") as f:        
        print("\n",f.read())
