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



#TASK3
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

#TASK16
name=input("student name :")
age=int(input("enter your  age :"))
rollnumber =int(input("enter your roll number :"))
collagename=input("enter your  collage name :")

print("name:",name )
print("age:",age)
print("roll number:",rollnumber)
print("collage name :",collagename)
def create_report():
  try:

    file=open('student_report.txt','w')
    file.write("student report \n")
    file.write("name"+name+"\n")
    file.write("age:"+str(age)+"\n")
    file.write("collage name:"+collagename+'\n')
    file.close()
    print("report  created  successfully!")
    logging.info("report crested successfully! ")

  except Exception as e:
    print("report creation failed1")
    logging.error("report failed:",+str(e))
logging.basicConfig(
  filename="execuation.log"'
  level=logging.INFO
)
schedule.every(1).minutes.do(create_report)
print("job started...")
print('report will be created every 1 minute.')
while True :
  schedule .rum_pending()
  time.sleep(1)


  #TASK 18
  import re
import time
import logging
Log_FILE="app.log"
ERROE_THRESHOLD=3
CHECK_INTERVAL=2
logging basicConfig(
    filename="alert.log"
    level=logging.WARNING,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
ERROR_PATTERN=re.compile(
    r"(ERRORICAITICALEXCEPTION)",
    re.IGNORECASE
)
def monitor_log():
    error_count=0

    print("Log monitoring started...")
    print("monitoring:",Log_FILE)
    with open(Log_FILE"r")as file:
       file.seek(0,2)
       while True:
           line=file.readline()
           if not line:
               time.sleep(CHECK_INTERVAL)
               continue
           line=line.strip()
           if ERROR_PATTERN.search(line):
               error_count+=1
               print("ERROR detected:",line)
               if error_count>=ERROE_THRESHOLD:
                   message=(
                       f"ALERT! error thershold crossed."
                       f"total errors:(error_count)"
                   )
                   print(message)
                   logging.warning(message)
                   error_count=0
if __name__=="__main__":
    monitor_log()
   

#TASK 19
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def home():
    return{'message':"Task managment API is working!"}
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
DATABASE_URL="sqlite:///./tasks.db"
engine = create_engine(
    DATABASE_URL
    connect_args={"check_same_thread":False}
)
SessionLocal =sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base=declarative_base()
from sqlalchemy import column ,Integer,String,Boolean,ForeignKey
from databas import Base
class User(Base):
    __tablename__="users"
    id=column(Integer,primary_key=True,index=True)
    username=column(String.unique=True,index=True)
    password=column(String)
class Task(Base):
    __tablename__="tasks"
    id=column(Integer,primary_key=True,index=True)
    tital=column(String)
    description=column(string)
    completed=column(Boolean,default=False)
    User_id=column(Integer,ForeignKey('user.id'))

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, User

app = FastAPI()


Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Task Management API is working!"}


@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.username == username).first()

    if existing_user:
        return {"message": "Username already exists"}

    new_user = User(
        username=username,
        password=password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "username": new_user.username
    }
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "my-secret-key"
ALGORITHM = "HS256"


def create_token(username):
    expire = datetime.utcnow() + timedelta(minutes=30)

    data = {
        "sub": username,
        "exp": expire
    }

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token

from auth import create_token


@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.username == username).first()

    if not user:
        return {"message": "User not found"}

    if user.password != password:
        return {"message": "Incorrect password"}

    token = create_token(user.username)

    return {
        "message": "Login successful",
        "access_token": token
    }
# Create Task
@app.post("/tasks")
def create_task(
    title: str,
    description: str,
    username: str,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return {"message": "User not found"}

    new_task = Task(
        title=title,
        description=description,
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task created successfully",
        "task_id": new_task.id
    }


# Get User Tasks
@app.get("/tasks")
def get_tasks(username: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.username == username).first()

    if not user:
        return {"message": "User not found"}

    tasks = db.query(Task).filter(Task.user_id == user.id).all()

    return tasks


# Update Task
@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    title: str,
    description: str,
    username: str,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user.id
    ).first()

    if not task:
        return {"message": "Task not found"}

    task.title = title
    task.description = description

    db.commit()

    return {"message": "Task updated successfully"}


# Delete Task
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    username: str,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user.id
    ).first()

    if not task:
        return {"message": "Task not found"}

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}


    #TASK 20
    from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
import time 
app = FastAPI()
LIMIT=5
WINDOW=60
requests={}
@app.get("/")
def home():
    return {"message":"Rate limiting API is running"}
@app.get("/data")
def get_data(request:Request):
    client_ip=request.client.host
    current_time=time.time()
    if client_ip not in requests:
        requests[client_ip]={
            "count":1,
            "start_time":current_time
        }
        return {"message":"Request sucessful"}
    client_data= requests[client_ip]
    if current_time-client_data["start_time"]>=WINDOW:
        client_data["count"]=1
        client_data["start_time"]=current_time
        return{"message":'Request sucessful'}
    if client_data["count"]>=LIMIT:
        return JSONResponse(
            status_code=429,
            content={
                'error':'too many requests',
                'message':'Rate limit exceeded . Try again later.'
            }

        )
    client_data['count']+=1
    return{
        'message':'Request sucessful',
        'requests_used':client_data['count'],
        'limit':"LIMIT"
    }



















        




     


 


 num=int(input("enter your number::"))
for i in range(1,11):
    print(num,"x" ,i,"=" ,num*i)
   

#    
