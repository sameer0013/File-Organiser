with open("currency.txt","r") as f:
    lines=f.readlines()
  
dict={}  
for line in lines:
    lines2 =line.split("\t")  
    dict[lines2[0]]=lines2[1]
amount=int(input("enter the amount: "))
print("choose the currency you want to check: ")

[print(i+1,".",item) for i, item in  enumerate(dict.keys()) ]
      
currency=input("enter one of these:")
print(f"{currency} of your {amount}INR is {amount * float(dict[currency])}")      
      