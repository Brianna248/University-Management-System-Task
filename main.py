class person:
    def __init__ (self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def change_details(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
        #this allows me to change the details again in the future
        # it is structured in the same way as the __init__ function because it does the same thing  
    def get_details(self): #don't need to add parameters 
        return("Name:" + self.name + " Age:" + self.age + " Gender:" + self.gender) #use the parameters from __init__
#----------------------------------------------------------------------------------------------------------------------    
# testing if stuff works 
bob= person("bob", "23"," male")
bob.set_details("bob", "34", "male")
print(bob.get_details())
#----------------------------------------------------------------------------------------------------------------------
class student(person):
    def __init__ (self, name, age, gender, student_id, course):
        super().__init__(self, name, age, gender)
        self.student_id=student_id
        self.course=course 
        self.grades=[]
        # i must pass the new variables i'm adding into the function from the start as parameters
        # i do not need to pass in the new list i made as a parameter

    def change_student_details(self, student_id, course):
        self.student_id=student_id 
        self.course=course 
         #this allows me to change the details again in the future
        # it is structured in the same way as the __init__ function because it does the same thing  

    def add_grade(self, grade):
        self.grade= grade
        super().__init__(self, name, age, gender, student_id, course)
        self.grades.append(self.grade)

    def calculate_average_grade(self):# don't need details from the specific function, can just take them from 'self' 
        if len(self.grades)==0:
            return("0")
        else: 
            grade_sum=sum(self.grades)
            n=int(len(self.grades))
            avg_grade= (grade_sum/n)
            return("Average Grade: " + avg_grade + "Number of grades added: " + n)
        
    def get_student_summary(self, name, age, gender, student_id, course, avg_grade): 
        return(" Name: " + self.name +
               " Age: " + self.age +
               " Gender: " + self.gender +
               " Sudent ID: " + self.course +
               self.calculate_average_grade() )

# if a variable I need is external then I need to call it in as a parameter
# if i'm using variables from within the class I always need to start the variable i'm calling upon with 'self.'
