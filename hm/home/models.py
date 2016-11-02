from django.db import models
# Create your models here.

SEMESTER = (
    (1,'I'),(2,'II'),(3,'III'),(4,'IV'),(5,'V'),(6,'VI'),(7,'VII'),(8,'VIII'),(9,'IX'),(10,'X'),
)
DEPARTMENT = (
    ('CSE','Computer Science & Engg'),
    ('MECH','Mechanical Engg'),
    ('CIV','Civil Engg'),
    ('MNC','Mathematics & Computing'),
    ('EEE','Electrical Engg'),
)
PROGRAM =(
    ('BTECH','B.Tech'),
    ('IDD','IDD'),
    ('IMD','IMD'),
    ('MTECH','M.Tech'),
    ('PHD','Phd'),
)


class Hostel(models.Model):
    name = models.CharField(max_length=100,unique=True,default='')
    fullname = models.CharField(max_length=200,null=True, blank=True)


class Student(models.Model):
    roll = models.BigIntegerField(primary_key=True,default=None)
    name = models.CharField(max_length=100,default='')
    dob = models.DateField(default='1/1/1996')
    email = models.EmailField(default='')
    mobile = models.BigIntegerField(default=None)
    program = models.CharField(max_length=10,choices=PROGRAM,default='')
    department = models.CharField(max_length=10,choices=DEPARTMENT,default='')
    semester = models.IntegerField(choices=SEMESTER,default=None)
    father_name = models.CharField(max_length=100,default='')
    mother_name = models.CharField(max_length=100,default='')
    father_occ = models.CharField(max_length=100,default='')
    mother_occ = models.CharField(max_length=100,default='')
    parent_contact = models.BigIntegerField(default=None)
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT,default='')
    room = models.CharField(max_length=10,default='')
    du = models.CharField(max_length=100,default='')
    mess_du = models.CharField(max_length=100,default='')
    guardian_name = models.CharField(max_length=100,null=True, blank=True)
    local_address = models.CharField(max_length=500,null=True, blank=True)
    relation = models.CharField(max_length=100,null=True, blank=True)
    guardian_contact = models.BigIntegerField(null=True, blank=True)
    permanent_address = models.CharField(max_length=500,default='')
    town = models.CharField(max_length=100,default='')
    state = models.CharField(max_length=100,default='')
    pincode = models.IntegerField(default=None)
    account = models.BigIntegerField(default=None)
    bank_name = models.CharField(max_length=100,default='')
    branch_name = models.CharField(max_length=100,default='')
    ifsc = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=100,default='')


class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    id = models.IntegerField(primary_key=True, default=None)
    type = models.CharField(max_length=100,default='')
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE,default='')
    complaint = models.CharField(max_length=100,default='')
    time = models.DateTimeField(default=None)


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True,default=None)
    name = models.CharField(max_length=100,default='')
    designation = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100,default='')
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT,default='')
    email = models.EmailField(default='')

