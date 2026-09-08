#student data 
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
