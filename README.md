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




def add_task():
    task=input("enter your task :")
    task.append(task)
    print("task added successfully!")

def view_tasks():
    if len(tasks)==0:
        print("no tasks available")
    else:
        print("/n your tasks:")
        for i in range (len(tasks)):
            print(i+1,"."tasks(i))

def update_task():
    view_tasks()
    if len(tasks)>0:
        number=int(input("enter task number to update:"))
        if number>=1 and number<=len(tasks):
            tasks.pop(number - 1)
            print("tasks deleted successflly !")
        else:
            print("invalid task number. ")

while True:
    print("/n===TO DO LIST===")
    print("1.ADD TASK ")
    print("2. view task")
    print("3.update task")
    print("4.delete task")
    print("5. exit")

    choice=input("enter your choice:")

    if choice =="1":
        add_task()
    elif choice=='2':
        view_tasks()
    elif choice=="3":
        update_task()
    elif choice=="4":
        delete_task()
    elif choice=="5":
        print("thank you !")
        break
    else:
        print("invalid choice .please try again")


 


 num=int(input("enter your number::"))
for i in range(1,11):
    print(num,"x" ,i,"=" ,num*i)
   

#    
