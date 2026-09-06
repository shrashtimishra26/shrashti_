print("temperature converter")
print("1.celsius to fahrenheit")
print("2.fahrenheit to celsius")
print("3.celsisus to kelvin")
print("4.kelvin to celsius")

choice=int(input("enter  your choice:"))
temp=float(input("enter temperature:"))

if choice ==1:
    result=(temp*9/5)+32
    print("temperature =",result,"F")

elif choice==2:
    result=(temp-32*5/9)
    print("temperature =",result,"C")

elif choice==3:
    result=temp+273.15
    print("temperature =",result,"k")

elif choice==4:
    result=temp-273.15
    print("temperature =",result,"C")

else:
    print("Invalid choice")
