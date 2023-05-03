from django.db import models

# Create your models here.

# User
# id : int
# first_name: string
# last_name:string
# username:string
# password:string
# email:string

# login(username,password):boolean
# logout(id):boolean


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def login(self, username, password):
        return self.username == username and self.password == password

    def logout(self, id):
        return self.id == id

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Department(models.Model):
    DepID = models.AutoField(primary_key=True)
    DepName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.DepName


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    DoctorID = models.IntegerField()
    PatientID = models.IntegerField()
    Detail = models.CharField(max_length=100)
    DateOfAppointment = models.DateField()
    TimeOfAppointment = models.TimeField()
    Preferred_Time = models.DateTimeField()

    def autoPickDoctor(self):
        pass


class Patient(User):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def scheduleAnAppointment(self, id):
        pass

    def cancelAnAppointment(self, id):
        pass

    def viewAnAppointment(self, id):
        pass


class Doctor(User):
    specialty = models.CharField(max_length=100)
    workDate = models.DateField()
    DepID = models.ForeignKey(Department, on_delete=models.CASCADE)
    availability = models.DateTimeField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    description = models.TextField()

    def viewAnAppointments(self):
        pass

    def viewAnAppointment(self, id, patient):
        pass


class Secretary(User):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    description = models.TextField()
    DepID = models.ForeignKey(Department, on_delete=models.CASCADE)

    def scheduleAnAppointment(self, patient):
        pass

    def cancelAnAppointment(self, patient):
        pass

    def viewAnAppointment(self, id, patient):
        pass

    def viewAnAppointments(self, patient):
        pass
