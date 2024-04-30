from datetime import timezone
from itertools import count
from django.db import models
import uuid
from django.db import models
from django.db.models.signals import pre_save , post_save
from django.dispatch import receiver
import random
from django.db.models import Count, Avg
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

def generate_unique_po_number():
    return str(random.randint(10000, 99999))

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class Usermodel(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    PRIORITY_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),

)   
    usertypes = (
    ('Student', 'Student'),
    ('Institute', 'Institute'),
    ('Other', 'Other'),
    

)
    # boards = (('West Bengal Board of Secondary Education (WBBSE)','West Bengal Board of Secondary Education (WBBSE)'),('West Bengal Council for Higher Secondary Education (WBCHSE)','West Bengal Council for Higher Secondary Education (WBCHSE)'),('Karnataka School Examination and Assessment Board (KSEAB)','Karnataka School Examination and Assessment Board (KSEAB)'),('Goa Board of Secondary and Higher Secondary Education (GBSHSE)','Goa Board of Secondary and Higher Secondary Education (GBSHSE)'),('Directorate of Higher Secondary Education, Kerala(DHSE)','Directorate of Higher Secondary Education, Kerala(DHSE)'),('DGE, Tamil Nadu','DGE, Tamil Nadu'),('Jharkhand Academic Council(JAC)','Jharkhand Academic Council(JAC)'),
    #           ('Board of Intermediate Education, Andhra Pradesh (BIEAP)','Board of Intermediate Education, Andhra Pradesh (BIEAP)'),('Board of Secondary Education, Assam (SEBA)','Board of Secondary Education, Assam (SEBA)'),('Tripura Board of Secondary Education (TBSE)','Tripura Board of Secondary Education (TBSE)'),('Council of Higher Secondary Education, Odisha','Council of Higher Secondary Education, Odisha'),('Chhattisgarh Board of Secondary Education (CGBSE)','Chhattisgarh Board of Secondary Education (CGBSE)'),('Telangana State Board of Intermediate Education (TSBIE)','Telangana State Board of Intermediate Education (TSBIE)'),('Board of Secondary Education, Odisha','Board of Secondary Education, Odisha'),('Board of Secondary Education, Madhya Pradesh (MPBSE)','Board of Secondary Education, Madhya Pradesh (MPBSE)'),('Board of School Education, Haryana (HBSE)','Board of School Education, Haryana (HBSE)'),('Bihar School Examination Board (BSEB)','Bihar School Examination Board (BSEB)'),('Nagaland Board of School Education (NBSE)','Nagaland Board of School Education (NBSE)'),('Council of Higher Secondary Education, Manipur (COHSEM)','Council of Higher Secondary Education, Manipur (COHSEM)'),('Board of Secondary Education, Rajasthan (RBSE)','Board of Secondary Education, Rajasthan (RBSE)'),('Maharashtra State Board of Secondary and Higher Secondary Education (MSBSHSE)','Maharashtra State Board of Secondary and Higher Secondary Education (MSBSHSE)'),('Uttarakhand Board of School Education (UBSE)','Uttarakhand Board of School Education (UBSE)'),('Assam Higher Secondary Education Council (AHSEC)','Assam Higher Secondary Education Council (AHSEC)'),('Mizoram Board of School Education (MBSE)','Mizoram Board of School Education (MBSE)'),('Himachal Pradesh Board of School Education (HPBOSE)','Himachal Pradesh Board of School Education (HPBOSE)'),('Board of Secondary Education, Manipur (BSEM)','Board of Secondary Education, Manipur (BSEM)')('Meghalaya Board of School Education (MBOSE)','Meghalaya Board of School Education (MBOSE)'),('Jammu and Kashmir Board of School Education (JKBOSE)','Jammu and Kashmir Board of School Education (JKBOSE)'),)
    username = models.CharField(max_length=45)
    custom_id = models.CharField(max_length=8,blank = True,editable=False,unique=True)
    date_of_birth = models.DateField(null=True)
    profile_image = models.ImageField(upload_to='Authorised/profile_images/',blank=True)
    
    
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    groups = models.ManyToManyField(
        Group,
        related_name="userkap_groups",  # unique related_name
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="userkap_user_permissions",  # unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    def __str__(self):
        return self.username

@receiver(pre_save, sender=Usermodel)
def generate_custom_id(sender, instance, **kwargs):
    # Check if custom_id is not set
    if not instance.custom_id:
        # Start counting from 1
        for i in count(start=1):
            # Format the count as a 4-digit string
            formatted_count = f"{i:05}"

            # Create the custom_id by concatenating '5' and the formatted count
            custom_id = f"12{formatted_count}"

            # Check if a Tags instance with this custom_id already exists
            if not Usermodel.objects.filter(custom_id=custom_id).exists():
                # Set the generated custom_id for the instance
                instance.custom_id = custom_id
                break


class Vendor(models.Model):
    vendor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name
    

class PurchaseOrder(models.Model):
    purchase_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    po_number = models.CharField(max_length=5, unique=True, default=generate_unique_po_number,editable =False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    completion_date = models.DateTimeField(default = "")
    items = models.JSONField()
    quantity = models.IntegerField()
    CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("In-Progress","In-Progress"),
        ("Canceled", "Canceled"),
    ]
    status = models.CharField(
    max_length=50,
    choices=CHOICES,
    default='Other',blank=True)
    
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

@receiver(pre_save, sender=PurchaseOrder)
def generate_unique_po_number(sender, instance, **kwargs):
    if not instance.po_number:
        instance.po_number = generate_unique_po_number()
        
@receiver(pre_save, sender=PurchaseOrder)
def update_completion_date(sender, instance, **kwargs):
    if instance.status == 'Completed':
        PurchaseOrder.objects.filter(vendor=instance, status='Completed').update(completion_date=timezone.now())

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, created, **kwargs):
    if instance.status == 'Completed':
        vendor = instance.vendor
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='Completed')
        total_pos = PurchaseOrder.objects.filter(vendor=vendor)

        if total_pos.exists():
            fulfillment_rate = completed_pos.count() / total_pos.count()
        else:
            fulfillment_rate = 0
        
        if instance.quality_rating is not None:
            completed_pos_with_quality_rating = completed_pos.filter(quality_rating__isnull=False)
            quality_rating_avg = completed_pos_with_quality_rating.aggregate(Avg('quality_rating'))['quality_rating__avg']
        else:
            quality_rating_avg = None

        if instance.acknowledgment_date:
            response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() / 3600
                              for po in completed_pos.exclude(acknowledgment_date__isnull=True)]
            average_response_time = sum(response_times) / len(response_times) if response_times else 0
        else:
            average_response_time = None

        on_time_deliveries = completed_pos.filter(delivery_date__lte=instance.delivery_date).count()
        total_completed_pos = completed_pos.count()
        on_time_delivery_rate = on_time_deliveries / total_completed_pos if total_completed_pos > 0 else 0

        # Create or update HistoricalPerformance instance
        HistoricalPerformance.objects.update_or_create(
            vendor=vendor,
            date=instance.delivery_date,
            defaults={
                'on_time_delivery_rate': on_time_delivery_rate,
                'quality_rating_avg': quality_rating_avg,
                'average_response_time': average_response_time,
                'fulfillment_rate': fulfillment_rate
            }
        )

class HistoricalPerformance(models.Model):
    performance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
