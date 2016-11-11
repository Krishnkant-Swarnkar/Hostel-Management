from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
# Create your models here.
mobile_regex = RegexValidator(regex=r'^[6789]\d{9}$', message="Enter a valid 10 digit mobile number(No 0 or country code needed.)")
roll_regex = RegexValidator(regex=r'^[1-9]\d{7}$', message="Enter a valid roll number.")
pin_regex = RegexValidator(regex=r'^[1-9]\d{5}$', message="Enter a valid Pincode.")
ac_regex = RegexValidator(regex=r'^\d{9,18}$', message="Enter a valid Account number.")
ifsc_regex = RegexValidator(regex=r'^[A-Za-z]{4}\d{7}$', message="Enter a valid IFSC code.")
du_regex = RegexValidator(regex=r'^DU\d{8}$', message="Enter a valid DU reference number.")
room_regex = RegexValidator(regex=r'^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$', message="Enter a valid room number.")
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
COMPLAINT_TYPE=(
    ('Water Supply','Water Supply'),
    ('Electricity','Electricity'),
    ('Lan Port','Lan Port'),
    ('Furniture','Furniture'),
    ('Canteen','Canteen'),
    ('Registration','Registration'),
    ('Security','Security'),
    ('Parking','Parking'),
    ('Mess','Mess'),
    ('Disturbance','Disturbance'),
    ('Other Infra-related','Other Infra-related'),
    ('Cleanliness','Cleanliness'),
    ('Suggestion','Suggestion'),
    ('Others','Others')
)


class Hostel(models.Model):
    name = models.CharField(max_length=100,unique=True,default='')
    fullname = models.CharField(max_length=200,null=True, blank=True)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    roll = models.CharField(primary_key=True,default=None,validators=[roll_regex],max_length=8)
    name = models.CharField(max_length=100,default='')
    dob = models.DateField(default='1/1/1996')
    email = models.EmailField(default='')
    mobile = models.CharField(default=None,validators=[mobile_regex],max_length=10)
    program = models.CharField(max_length=10,choices=PROGRAM,default='')
    department = models.CharField(max_length=10,choices=DEPARTMENT,default='')
    semester = models.IntegerField(choices=SEMESTER,default=None)
    father_name = models.CharField(max_length=100,default='')
    mother_name = models.CharField(max_length=100,default='',null=True, blank=True)
    father_occ = models.CharField(max_length=30,default='')
    mother_occ = models.CharField(max_length=30,default='',null=True, blank=True)
    parent_contact = models.CharField(default=None,validators=[mobile_regex],max_length=10)
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT,default='')
    room = models.CharField(max_length=5,default='',validators=[room_regex])
    du = models.CharField(max_length=10,validators=[du_regex],default='')
    mess_du = models.CharField(max_length=10,validators=[du_regex],default='')
    local_address = models.CharField(max_length=500,null=True, blank=True)
    local_contact = models.CharField(null=True, blank=True,validators=[mobile_regex],max_length=10)
    permanent_address = models.CharField(max_length=500,default='')
    town = models.CharField(max_length=50,default='')
    state = models.CharField(max_length=50,default='')
    pincode = models.CharField(default=None,validators=[pin_regex],max_length=6)
    account = models.CharField(default=None,validators=[ac_regex],max_length=15)
    holder =  models.CharField(max_length=100,default='')
    bank = models.CharField(max_length=100,default='')
    branch = models.CharField(max_length=100,default='')
    ifsc = models.CharField(max_length=11,validators=[ifsc_regex],default='')
    password = models.CharField(max_length=20,default='')

    def __unicode__(self):
        return self.roll


class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    type = models.CharField(max_length=25,default='',choices=COMPLAINT_TYPE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE,default='')
    complaint = models.CharField(max_length=500,default='')
    time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True,default=None)
    name = models.CharField(max_length=100,default='')
    designation = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100,default='')
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT,default='')
    email = models.EmailField(default='')

