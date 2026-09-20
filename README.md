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

# TASK 21



from fastapi import FastAPI
import redis 
import time 
import json 
app = FastAPI()
r = redis.Redis(
    host='localhot',
    port=6379,
    decode_responses=True
)
def get_data_from_database(item_id):
    time.sleep(2)
    return(
        "id":item_id,
        "name":"student",
        "course":"AI",
        "message":"data fetched from database"
    )
@app.get("/data/{item_id}")
def get_data(item_id:int):
    start_time=time.time()
    cached_data=r.get(f"item:(item_id)")
    if cached_data:
        data=json.loads(cached_data)
        source="CACHE"
    else:
        data =get_data_from_database(item_id)
        source ="DATABASE"

        r.setex(
            f"item:{item_id}",
            60,json.dumps(data)
        
        )
        end_time=time.time()
        return {
            "data":data,
            "source":source,
            "response_time":round(end_time-start_time,4)

        }
    @app.delete("/cache/{item_id}")
    def delete_cache(item_id:int):
        deleted=r.delete(f"item:{item_id}")
        if deleted:
            return{
                "message":"cache dleted sucessfully "
                }
        return{
            'message':"caches was not found "
        }




#TASK 22





from celery import celery 
import time 
celery_app=celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"

)
@celery_app.task
def process_job(job_id):
    print(f"job(job_id)started")
    time.sleep(10)
    print(f"job(jon_id)completed")
    return f"job(job_id)completed sucessfully"
from fastapi import FastAPI
from worker import process_job
app=FastAPI()
@app.get("/")
def home():
    return{
        'message':'Background job processer is running'
    }
@app.post("/submit")
def submit_job():
    task=process_job.delay('job-1')
    return{
        "job_id":task.id
        "message":"job submitted sucessfully "
    }
@app.get("/status/{job_id}")
def check_status(job_id:str):
    task=process_job.AsyncResult(job_id)
    if task.state=="PENDING":
        status="PENDING"
    elif task.state=="STATRTED":
        status="Running "
    elif task.state=="FAILURE":
        status="failed"
    else:
        status=task.state
    return{
        "job_id":job_id,
        "status":status,
        "result":task.result if task.state=="sucess"else none 

    }

   

#    TASK 23


import requests
import time
from concurrent.futures import ThreadPoolExecutor


def check_url(url):
    try:
        start_time = time.time()

        response = requests.get(url, timeout=5)

        end_time = time.time()

        response_time = end_time - start_time

        return {
            "url": url,
            "status": response.status_code,
            "response_time": response_time,
            "success": True
        }

    except requests.RequestException as e:
        return {
            "url": url,
            "status": "Failed",
            "response_time": None,
            "success": False,
            "error": str(e)
        }


# URLs to check
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://example.com"
]


# Create threads
with ThreadPoolExecutor(max_workers=5) as executor:

    results = executor.map(check_url, urls)


# Display report
print("\n========== URL CHECKER REPORT ==========\n")

for result in results:

    print("URL:", result["url"])

    if result["success"]:
        print("Status Code:", result["status"])
        print("Response Time:",
              round(result["response_time"], 3), "seconds")




  #TASK 25

import threading
import _multiprocessing
import asyncio
import time 
def thread_task(task_number):
    print(f'thread task{task_number}started')
    time.sleep(2)
    print (f'thread task{task_number}completed')
def run_threading():
    print("\n---THREADING---")
    start=time.time()
    threads=[]
    for i in range(1,6):
        t=threading.Thread(target=thread_task,args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end=time.time()
    print("threading time:",round(end-start,2),"seconds")
async def async_task(task_number):
    print(f'Async Task{task_number}completed')
async def run_asyncio():
    print("\n---ASYNCIO---")
    start=time.time()
    print("AsyncIO Time:",round(end-start,2),"seconds")
def cpu_task(number):
    total=0
    for i in range(1,5_000_000):
        total+=i*i
    return total 
def run_multiprocessing():
    print('\n---_multiprocessing---')
    start=time.time()
    with multiprocessing.Pool(processes=4)as pool:
        results=pool.map(cpu_task,range(4))
    end=time.time()
    print("Multiprocessing Time: ",round(end-start,2),'seconds')
if__name__=="__main__":
    run_threading()
    asyncio.run(run_asyncio())
    run_multiprocessing()
    print("\n---COMPARISON COMPLETED---")





  

    else:
        print("Status:", result["status"])
        print("Error:", result["error"])

    print("----------------------------------------")


    # TASK 27


    import pandas as pd
import numpy as np


# -----------------------------------
# 1. LOAD DATASET
# -----------------------------------

file_name = input("Enter CSV file name: ")

try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print("File not found! Please check the file name.")
    exit()


print("\n====================================")
print("       DATA QUALITY REPORT")
print("====================================")


# -----------------------------------
# 2. BASIC INFORMATION
# -----------------------------------

print("\n--- BASIC INFORMATION ---")

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn names:")
for column in df.columns:
    print("-", column)


# -----------------------------------
# 3. DATA TYPES
# -----------------------------------

print("\n--- DATA TYPES ---")

print(df.dtypes)


# -----------------------------------
# 4. MISSING VALUES
# -----------------------------------

print("\n--- MISSING VALUES ---")

missing_values = df.isnull().sum()

for column in df.columns:
    print(column, ":", missing_values[column])


# -----------------------------------
# 5. DUPLICATE RECORDS
# -----------------------------------

print("\n--- DUPLICATE RECORDS ---")

duplicates = df.duplicated().sum()

print("Total duplicate rows:", duplicates)


# -----------------------------------
# 6. UNIQUE VALUES
# -----------------------------------

print("\n--- UNIQUE VALUE COUNTS ---")

for column in df.columns:
    print(column, ":", df[column].nunique())


# -----------------------------------
# 7. COMPLETENESS
# -----------------------------------

print("\n--- COMPLETENESS ---")

total_values = df.size
missing_total = df.isnull().sum().sum()

completeness = ((total_values - missing_total) / total_values) * 100

print("Completeness:", round(completeness, 2), "%")


# -----------------------------------
# 8. UNIQUENESS
# -----------------------------------

print("\n--- UNIQUENESS ---")

for column in df.columns:

    unique_count = df[column].nunique()
    total_count = len(df)

    uniqueness = (unique_count / total_count) * 100

    print(
        column,
        ":",
        round(uniqueness, 2),
        "%"
    )


# -----------------------------------
# 9. INVALID / UNEXPECTED DATA TYPES
# -----------------------------------

print("\n--- DATA TYPE CHECK ---")

for column in df.columns:

    if df[column].dtype == "object":

        print(
            column,
            "-> Text/String data"
        )

    elif np.issubdtype(df[column].dtype, np.number):

        print(
            column,
            "-> Numeric data"
        )

    else:

        print(
            column,
            "-> Unexpected data type"
        )


# -----------------------------------
# 10. SUSPICIOUS RECORDS
# -----------------------------------

print("\n--- SUSPICIOUS RECORDS ---")

numeric_columns = df.select_dtypes(
    include=np.number
).columns


if len(numeric_columns) > 0:

    for column in numeric_columns:

        mean = df[column].mean()
        std = df[column].std()

        # Values far away from normal range
        suspicious = df[
            (df[column] > mean + 3 * std) |
            (df[column] < mean - 3 * std)
        ]

        print(
            column,
            "-> Suspicious records:",
            len(suspicious)
        )

else:

    print("No numeric columns found.")


# -----------------------------------
# 11. SAVE REPORT
# -----------------------------------

report = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isnull().sum().values,
    "Unique Values": [
        df[column].nunique()
        for column in df.columns
    ]
})


report.to_csv(
    "data_quality_report.csv",
    index=False
)


print("\n====================================")
print("Report generated successfully!")
print("File: data_quality_report.csv")
print("====================================")


#TASK 28
import pandas as pd
from difflib import SequenceMatcher
import re

# -------------------------------------------------
# 1. LOAD DATASET
# -------------------------------------------------

input_file = "customers.csv"

df = pd.read_csv(input_file)

print("Original Dataset:")
print(df)
print("\nTotal records:", len(df))


# -------------------------------------------------
# 2. TEXT NORMALIZATION
# -------------------------------------------------

def normalize_text(text):
    if pd.isna(text):
        return ""

    text = str(text).lower()
    
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)
    
    # Remove special characters
    text = re.sub(r"[^a-z0-9 ]", "", text)
    
    return text.strip()


# Normalize important fields

df["name_clean"] = df["name"].apply(normalize_text)
df["email_clean"] = df["email"].apply(normalize_text)
df["phone_clean"] = df["phone"].apply(normalize_text)


# -------------------------------------------------
# 3. EXACT DUPLICATE DETECTION
# -------------------------------------------------

exact_duplicates = df[
    df.duplicated(
        subset=["name_clean", "email_clean", "phone_clean"],
        keep=False
    )
]

print("\nExact Duplicates:")
print(exact_duplicates)


# Save exact duplicate report

exact_duplicates.to_csv(
    "exact_duplicate_report.csv",
    index=False
)


# -------------------------------------------------
# 4. FUZZY MATCHING FUNCTION
# -------------------------------------------------

def similarity(text1, text2):
    return SequenceMatcher(
        None,
        str(text1),
        str(text2)
    ).ratio()


# -------------------------------------------------
# 5. FIND POTENTIAL DUPLICATES
# -------------------------------------------------

potential_duplicates = []

for i in range(len(df)):

    for j in range(i + 1, len(df)):

        name_score = similarity(
            df.loc[i, "name_clean"],
            df.loc[j, "name_clean"]
        )

        email_score = similarity(
            df.loc[i, "email_clean"],
            df.loc[j, "email_clean"]
        )

        phone_score = similarity(
            df.loc[i, "phone_clean"],
            df.loc[j, "phone_clean"]
        )

        # Calculate average similarity
        average_score = (
            name_score +
            email_score +
            phone_score
        ) / 3

        # Potential duplicate condition
        if average_score >= 0.75:

            potential_duplicates.append({
                "record_1": i,
                "record_2": j,
                "name_similarity": round(name_score, 2),
                "email_similarity": round(email_score, 2),
                "phone_similarity": round(phone_score, 2),
                "average_similarity": round(average_score, 2)
            })


# Convert result to DataFrame

potential_df = pd.DataFrame(
    potential_duplicates
)


# -------------------------------------------------
# 6. SAVE POTENTIAL DUPLICATE REPORT
# -------------------------------------------------

potential_df.to_csv(
    "potential_duplicate_report.csv",
    index=False
)

print("\nPotential Duplicates:")
print(potential_df)


# -------------------------------------------------
# 7. CREATE CLEANED DATASET
# -------------------------------------------------

# Remove exact duplicates
cleaned_df = df.drop_duplicates(
    subset=["name_clean", "email_clean", "phone_clean"],
    keep="first"
)

# Remove helper columns
cleaned_df = cleaned_df.drop(
    columns=[
        "name_clean",
        "email_clean",
        "phone_clean"
    ]
)

# Save cleaned dataset

cleaned_df.to_csv(
    "cleaned_dataset.csv",
    index=False
)


# -------------------------------------------------
# 8. FINAL OUTPUT
# -------------------------------------------------

print("\n--------------------------------")
print("DUPLICATE DETECTION COMPLETED")
print("--------------------------------")

print("Original records :", len(df))
print("Cleaned records  :", len(cleaned_df))
print("Exact duplicates :", len(exact_duplicates))
print("Potential pairs  :", len(potential_df))

print("\nFiles created:")
print("1. exact_duplicate_report.csv")
print("2. potential_duplicate_report.csv")
print("3. cleaned_dataset.csv")

