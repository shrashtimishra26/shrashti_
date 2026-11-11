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





## micro project 


## project screenshots 
<img width="919" height="616" alt="login page" src="https://github.com/user-attachments/assets/4d782678-330a-4f75-9aea-2b7f6005514a" />

<img width="971" height="572" alt="image" src="https://github.com/user-attachments/assets/89c8ba4e-42ad-4095-ba30-2a1f43cf3ac0" />

<img width="946" height="554" alt="image" src="https://github.com/user-attachments/assets/f5e3aa70-dee6-4ecb-bfb0-86198afdbe69" />

<img width="964" height="585" alt="image" src="https://github.com/user-attachments/assets/bb91869a-5a77-40bb-b8aa-dfd021f06001" />

<img width="971" height="605" alt="image" src="https://github.com/user-attachments/assets/f0fff1b8-f1b1-4105-8856-ff18d70dd4a2" />

<img width="938" height="467" alt="image" src="https://github.com/user-attachments/assets/7ecaece2-7a89-40a4-93ba-1e756d11362b" />

## Technology used 


python [backend]
HTML   [web structure]
CSs    [web design]
jinja2  [dynamic templates]
Flask  [web framework]


## About projects


developing a web application using technologies like HTML, CSS,and Python. GitHub is used to store the project files, track code changes, and manage development.



## project structure


Multi-User Portfolio Website
│
├── app.py
├── templates/
│   ├── login.html
│   ├── shrashti.html
│   
│
├── static/
│   ├── css/
│   └── images/


##  login page code 


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOGIN  PAGE</title>
    <link rel="stylesheet" href="{{url_for('static',filename='css/login.css')}}">
</head>
<body>
    <div class="login-container">
        <h1>WELCOME BACK !</h1>
        <p>Login to access your portfolio</p>
        
        <form action="{{ url_for('login') }}" method="POST">
            <label for="username">Username</label>
            <input
            type="text"
            id="username"
            name="username"
            placeholder="Enter your name"
            required
            >
            <label for="password">password</label>
            <input 
            type="password"
            id="password"
            name="password"
            placeholder="enter your password"
            required
            >
            <button type="submit">Login</button>
        </form>
        <p class="footer-text">
            Student portfolio website
        </p>
    </div>
</body>
</html>





## python flask code 


from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

app.secret_key = "my_portfolio_secret_key"

users = {
    "shrashti": {
        "password": "@mishra",
        "page": "shrashti.html"
    },

    "yashika": {
        "password": "@sharma",
        "page": "yashika.html"
    }
}

@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("portfolio"))

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username", "").strip().lower()
    password = request.form.get("password", "")

    if username in users and password == users[username]["password"]:

        session["username"] = username

        print("LOGIN SUCCESSFUL:", username)

        return redirect(url_for("portfolio"))

    print("LOGIN FAILED:", username)

    return render_template(
        "login.html",
        error="Invalid username or password!"
    )

@app.route("/portfolio")
def portfolio():

    if "username" not in session:
        return redirect(url_for("home"))

    username = session["username"]

    page = users[username]["page"]

    return render_template(page)

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)



## HTML code 



<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Shrashti Mishra | Portfolio</title>

    <link rel="stylesheet"
    href="{{ url_for('static', filename='css/shrashti.css') }}"
    >
</head>

<body>

    <!-- SIDEBAR -->

    <aside class="sidebar">

        <div class="logo">SM.</div>

        <nav>
            <a href="#home" class="active">⌂ &nbsp; Home</a>
            <a href="#about">♙ &nbsp; About</a>
            <a href="#projects">▣ &nbsp; Projects</a>
            <a href="#skills">〈〉 &nbsp; Skills</a>
            
            <a href="#contact">✉ &nbsp; Contact</a>
            <a href="#connect">◉ &nbsp; Connect</a>
        </nav>

        <a href="/logout" class="logout">↪ Logout</a>

    </aside>


    <!-- MAIN CONTENT -->

    <main>

        <!-- HOME -->

        <section id="home" class="hero">

            <p class="small-heading">WELCOME TO MY PORTFOLIO</p>

            <h1>
                Hi, I'm<br>
                <span>Shrashti Mishra</span>
            </h1>

            <h2>BTech AI Student </h2>

            <p class="description">
                I am a motivated and detail-oriented student
                passionate about technology, programming and
                Artificial Intelligence. I enjoy learning new
                technologies, developing projects and improving
                my technical skills.
            </p>

            <div class="buttons">
                <a href="#projects" class="primary-btn">
                    View My Work &nbsp; →
                </a>

                <a href="#contact" class="secondary-btn">
                    Get in Touch
                </a>
            </div>

        </section>


        <!-- ABOUT -->

        <section id="about" class="content-section">

            <p class="small-heading">GET TO KNOW ME</p>

            <h2>About <span>Me</span></h2>

            <div class="about-content">

                
                <img src="{{ url_for('static', filename='images/shrashti.jpeg.jpeg') }}"
     alt="Shrashti Mishra">
                <div>
                    <h3>Career Objective</h3>

                    <p>
                        Motivated and detail-oriented student with
                        a strong interest in technology, programming,
                        and continuous learning. Seeking opportunities
                        to enhance technical skills, contribute to
                        real-world projects, and build a successful
                        career in software development.
                    </p>
                </div>

            </div>

        </section>

        <section id="education" class="content-section">

            <p class="small-heading">MY ACADEMIC JOURNEY</p>

            <h2>My <span>Education</span></h2>

            <div class="info-card">
                <h3>Bachelor of Technology</h3>
                <p>Madhav Institute of Technology and Science, Gwalior</p>
                <p>Branch: Artificial Intelligence</p>
                <p>Currently Pursuing</p>
            </div>

            <div class="info-card">
                <h3>Class 12th</h3>
                <p>Percentage: 76.6%</p>
            </div>

            <div class="info-card">
                <h3>Class 10th</h3>
                <p>Percentage: 80%</p>
            </div>

        </section>

        <section id="projects" class="content-section">

            <p class="small-heading">WHAT I HAVE BUILT</p>

            <h2>My <span>Projects</span></h2>

            <div class="project-grid">

                <div class="info-card">
                    <h3>Calculator</h3>
                    <p>A basic calculator developed using Python.</p>
                    <span>Python</span>
                </div>

                <div class="info-card">
                    <h3>Temperature Converter</h3>
                    <p>A program to convert temperature units.</p>
                    <span>Python</span>
                </div>

                <div class="info-card">
                    <h3>Personal Portfolio</h3>
                    <p>A personal portfolio website.</p>
                    <span>HTML • CSS</span>
                </div>

                <div class="info-card">
                    <h3>Shopping Bill Generator</h3>
                    <p>A program to calculate shopping bills.</p>
                    <span>Python</span>
                </div>

                <div class="info-card">
                    <h3>Word and Character Counter</h3>
                    <p>Counts words and characters in a given text.</p>
                    <span>Python</span>
                </div>

                <div class="info-card">
                    <h3>Student Registration Form</h3>
                    <p>A frontend student registration form.</p>
                    <span>HTML</span>
                </div>

            </div>

        </section>

        <section id="skills" class="content-section">

            <p class="small-heading">MY TECHNICAL KNOWLEDGE</p>

            <h2>My <span>Skills</span></h2>

            <div class="skill-list">
                <span>HTML</span>
                <span>CSS</span>
                <span>Git</span>
                <span>GitHub</span>
                <span>Python</span>
                
            </div>

        </section>

        <section id="contact" class="content-section">

            <p class="small-heading">LET'S TALK</p>

            <h2>Contact <span>Me</span></h2>

            <div class="info-card">
                <p>Email: shrashtimishra722@gmail.com</p>
                <p>Phone: 7748902622</p>
                <p>Location: Gwalior, Madhya Pradesh</p>
            </div>

        </section>

        <section id="connect" class="content-section">

            <p class="small-heading">FIND ME ONLINE</p>

            <h2>Let's <span>Connect</span></h2>

            <div class="buttons">

                <a href="https://github.com/shrashtimishra26/shrashti_"
                   target="_blank" class="primary-btn">
                    GitHub →
                </a>

                <a href="https://www.linkedin.com/in/shrashti-mishra-514819409?utm_source=share_via&utm_content=profile&utm_medium=member_android"
                   target="_blank" class="secondary-btn">
                    LinkedIn →
                </a>

            </div>

            <p class="declaration">
                I hereby declare that all the above information
                is true to the best of my knowledge and belief.
                <br><br>
                — Shrashti Mishra
            </p>

        </section>


        <footer>
            © 2026 Shrashti Mishra. All Rights Reserved.
        </footer>

    </main>

</body>
</html>



