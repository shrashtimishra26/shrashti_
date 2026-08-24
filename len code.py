#len list me count btane ke liye use hota h 
fruits=["apple","orange","mango"]
print(len(fruits))

#insert kuch add krne ke liye use krte h 
fruits=["apple","orange","mango"]
fruits.insert(3,"grapes")
print(fruits)

#pop value de kr kisi bhi item ko remove krna 
fruits=["apple","orange","mango"]
fruits.pop(2)
print(fruits)

#sort number ko accending order me arrange kr deta h
num=[50,10,40,20,30]
num.sort()
print(num)

#reverse decending order me arrange kr deta h
num=[50,10,40,20,30]
num.reverse()
print(num)

#use of len,append,sort in single code 
num=[10,70,40,60,80]
num.sort()
num.append(50)
print(num)
print(len(num))

#loops+append
numbers=[]
for i in range(5):
    num=int(input("enter your number:"))
    numbers.append(num)
    numbers.sort()
print(numbers)

#logical question
numbers=[]
for i in range(5):
    num=int(input("enter number:"))
    numbers.append(num)

for num in numbers:
   if num%2==0:
    print(num )