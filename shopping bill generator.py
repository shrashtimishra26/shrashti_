print("===SHOPPING  BILL===")
coustmer=input("enter coustmer name:")
product1=input("enter product name :")
price1=float(input("enter price :"))
quantity1=int(input("enter quantity:"))

product2=input("enter product name: ")
price2=float(input("enter price :"))
quantity2=int(input("enter quantity:"))

product3=input("enter product name: ")
price3=float(input("enter price: "))
quantity3=int(input("enter quantity:"))

total1=price1* quantity1
total2=price2* quantity2
total3=price3* quantity3
subtotal = total1+total2+total3 

print ("coustmer name",coustmer)
print("prodect name =",product1 )
print("price =", price1)
print ("quantity =" ,quantity1)

print("prodect name =",product2 )
print("price =", price2)
print ("quantity =" ,quantity2)

print("prodect name =",product3 )
print("price =", price3)
print ("quantity =" ,quantity3)
print("total price :",subtotal)

print("____THANK YOU FOR SHOPPING____")