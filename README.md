#TASK 1


 num=int(input(" entre your number:"))
if num%2==0:
    print("even number")
elif num==0:
    print("this is zero")
    
else :
    print("odd number")

#TASK 2



print("====student grades calculator====")
name=input("entre your name:")
chemistry=int(input("entre your marks:"))
physics=int(input("entre your marks:"))
python=int(input("entre your marks:"))
mathmatics=int(input("entre your marks:"))
if  (chemistry<0 or chemistry>100 or python<0 or python>100 or physics<0 or physics>100
     or mathmatics,0 or mathmatics>100):
    

    total=chemistry+physics+python+mathmatics
    percentage=total/4
    print("____student result____")
    print("name:", name)
    print("total:",total)
    print("percentage:", percentage,"%")
    # marks grade 
    if percentage>=90:
           print("GRADE A+")
    elif percentage>=80:
           print(" GRADE A")
    elif percentage>=70 :
           print("GRADE B")
    elif percentage>=60:
           print("GRADE C")
    else:
           print("GRADE D")

else:
       print("invalid marks! marks should be bwt 0 and 100")

#TASK 14


print("temperature converter")
print("1.celsius to fahrenheit")
print("2.fahrenheit to celsius")
print("3.celsisus to kelvin")
print("4.kelvin to celsius")

choice=int(input("enter  your choice:"))
temp=float(input("enter temperature:"))

if choice ==1:
    result=(temp*9/5)+32
    print("temperature =",result"F")

elif choice==2:
    result=(temp-32*5/9)
    print("temperature =",result"C")

elif choice==3:
    result=temp+273.15
    print("temperature =",result"k")

elif choice==4:
    result=temp-273.15
    print("temperature =",result"C")

else:
    print("Invalid choice")

   #TASK 15 



   
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


