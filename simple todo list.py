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

