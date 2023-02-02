
class Person:
    moods = ('happy', 'tired', 'lazy')

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours >= 7:
            self.mood = self.moods[0]
        elif hours < 7 and hours > 0:
            self.mood = self.moods[1]
        else:
            self.mood = self.moods[2]
        return self.mood

    def eat(self, meals):
        if meals >= 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            self.healthRate = 0
        return self.healthRate

    def buy(self, items):
        self.money -= items * 10
        return self.money
class Employee(Person):
    def init(self, id, car, email, salary, distanceToWork, name, money, mood, healthRate):
        Person.init(self, name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = self.moods[0]
        elif hours > 8:
            self.mood = self.moods[1]
        else:
            self.mood = self.moods[2]
        return self.mood

    def drive(self, distance):
        self.car.run(distance)

    def refuel(self):
        self.car.fuelRate = 100

    def send_mail(self, to, subject, msg, receiver_name):
        email_file = open("{}_{}_{}.txt".format(receiver_name, self.name, subject), "w")
        email_file.write("From: {}\n".format(self.email))
        email_file.write("To: {}\n".format(to))
        email_file.write("Subject: {}\n".format(subject))
        email_file.write("Message: {}\n".format(msg))
        email_file.close()

class Office:
    def init(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        for employee in self.employees:
            print("Name:", employee.name)
            print("ID:", employee.id)
            print("Email:", employee.email)
            print("Salary:", employee.salary)
            print("-----------------------------")

    def get_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None

    def hire(self, employee):
        self.employees.append(employee)
        return "Employee hired successfully."

    def fire(self, id):
        employee = self.get_employee(id)
        if employee:
            self.employees.remove(employee)
            return "Employee fired successfully."
        return "Employee not found."

    def calculate_lateness(self, id, hours):
        employee = self.get_employee(id)
        if employee:
            if hours > 0:
                employee.salary -= (hours * 50)
                return "Employee salary deducted successfully."
            return "Hours should be greater than 0."
        return "Employee not found."

    def deduct(self, id, amount):
        employee = self.get_employee(id)
        if employee:
            employee.salary -= amount
            return "Employee salary deducted successfully."
        return "Employee not found."

    def reward(self, id, amount):
        employee = self.get_employee(id)
        if employee:
            employee.salary += amount
            return "Employee rewarded successfully."
        return "Employee not found."
class Car:
    def init(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, distance):
        self.fuelRate -= (distance / 10)
        return self.fuelRate

    def stop(self):
        self.velocity = 0
        return self.velocity
