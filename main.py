class Person:
    def __init__(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number

    def set_details(self, name, age , contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contact_number}")      


class Member(Person):
    def __init__(self, name, age, contact_number, membership_id, sport):
        super().__init__(name, age, contact_number)  
        self.membership_id = membership_id
        self.sport = sport
        self.performance_scores = []
    
    def set_member_details(self, membership_id, sport):
        self.membership_id = membership_id
        self.sport = sport
        self.performance_scores = []

    def add_performance_scores(self, score):
        self.performance_scores.append(score)

    def calculate_average_score(self):
        value = 0
        for score in self.performance_scores:
            value +=score
        average = value/ len(self.performance_scores)
        return(average)
    
    def get_member_summary(self):
        Member.get_details()
        print(f"Membership ID: {self.membership_id}, Average Performance Score: {Member.calculate_average_score()}")


class Coach(Person):
    def __innit__(self, name, age, contact_number, coach_id, specialisation, salary):
        super().__init__(name, age, contact_number)
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []


    def set_coach_details(self, coach_id, specialisation, salary):
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []           

    def assign_mentee(self, Member):
        self.mentees.append(Member.name + Member.sport)

    def get_mentees(self):
        print(self.mentees)

    def increase_salary(self,percentage):
        self.salary = self.salary * ((100+percentage)/100)


class Staff(Person):
    def __init__(self, name, age, contact_number, staff_id, position, years_of_service):
        super().__init__(name, age, contact_number)
        self.staff_id = staff_id
        self.postion = position
        self.years_of_service = years_of_service

    def set_staff_details(self, staff_id, position, years_of_service):
        self.staff_id = staff_id
        self.postion = position
        self.years_of_service = years_of_service

    def increment_years_of_service(self):
        self.years_of_service += 1

    def assist_member(self, Member):
        print(f"{self.name} assisted {Member.name} in resolving an issue")      

    def get_staff_summary(self):
        Staff.get_details()
        print(f"Staff ID: {self.staff_id}, Position: {self.position}, Years of service: {self.years_of_service}")


member1 = Member('John', 22, '07757493756', 'G8365', 'Football' )
member2 = Member('Emily', 24,'07794639646', 'H8689', 'Tennis', )
coach1 = Coach( 'Mark', 35, '077359632567', 'J7890', 'tennis', 30000 )
coach2 = Coach('Martha', 28, '07799247548', 'B9937', 'volleyball')
staff = Staff('Emma', 21, '07793659242', 'H7485', 'receptionist', 1)

coach1.assign_mentee(member2)
member1.add_performance_scores(45)
member1.add_performance_scores(52)
member1.calculate_average_score()
staff.assist_member(member2)
coach2.increase_salary(15)
staff.increment_years_of_service()

member1.get_member_summary()
member2.get_member_summary
staff.get_staff_summary()
