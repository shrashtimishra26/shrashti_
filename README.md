 num=int(input(" entre your number:"))
if num%2==0:
    print("even number")
elif num==0:
    print("this is zero")
    
else :
    print("odd number")


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


 num=int(input("enter your number::"))
for i in range(1,11):
    print(num,"x" ,i,"=" ,num*i)
   

#    
