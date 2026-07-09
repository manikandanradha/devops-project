name="Manikandan"
age=21
print("my name is",name,"my age is",age)


height = 5.8
is_engineer = True
print(type(height))
print(type(is_engineer))
native = input("my native place is;")
print("my native place is",native)



name1="Manikandan"
name2="agalya"
if name1==name2:
    print("both names are same")
else:
    print("no the names are wrong")
  
    
    
student_list= [   
    ["Mani",21],
    ["Sumii",17],
    ["Agalya",20],
    ["Pradhap",12]
 ]
for name,age in student_list:
    if age>=18:
        print(name,"you are eligible to get licence")
    else:
        print(name,"is not eligible to get licence")




def check_licence(name,age):
    if age>=18:
        print(name,"you are eligible to get licence")
    else:
        print(name,"is not eligible to get licence")

check_licence("ashok",16)


all_students = [
    {
        "name":"Manikandan",
        "age":21,
        "place":"kanyakumari",
        "course":"devops"
    },
    {
        "name":"Agalya",
        "age":20,
        "place":"kanyakumari",
        "course":"devops"
    },
    {
        "name":"Pradhap",
        "age":12,
        "place":"kanyakumari",
        "course":"devops"
    },
    {
        "name":"Sumi",
        "age":17,
        "place":"kanyakumari",
        "course":"devops"
    }
]

for student in all_students:
    print(student["name"])
    print(student["age"])
    print(student["place"])
    print(student["course"])
 