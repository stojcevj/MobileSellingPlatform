from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_first_name = models.CharField(max_length=50)
    profile_last_name = models.CharField(max_length=50)
    profile_date_of_birth = models.DateField()
    profile_phone_number = models.CharField(max_length=9)
    profile_email = models.EmailField()
    profile_password = models.CharField(max_length=70)
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    profile_image = models.ImageField(upload_to="images/profile/", null=True, blank=True)

    def __str__(self):
        return self.profile_first_name + " " + self.profile_email


class MobileListing(models.Model):
    PHONE_MAKE = (
        ("IPHONE", "Iphone"),
        ("SAMSUNG", "Samsung"),
        ("HUAWEI", "Huawei"),
        ("HTC", "Htc"),
        ("LG", "LG"),
        ("NOKIA", "Nokia"),
        ("BLACKVIEW", "Blackview"),
        ("OTHER", "Other")
    )

    PHONE_RAM_MEMORY = (
        ("1GB", "1Gb"),
        ("2GB", "2Gb"),
        ("3GB", "3Gb"),
        ("4GB", "4Gb"),
        ("6GB", "6Gb"),
        ("8GB", "8Gb"),
        ("12GB", "12Gb"),
        ("OTHER", "Other"),
    )

    PHONE_INTERNAL_MEMORY = (
        ("8GB", "8Gb"),
        ("16GB", "16Gb"),
        ("32GB", "32Gb"),
        ("64GB", "64Gb"),
        ("128GB", "128Gb"),
        ("256GB", "256Gb"),
        ("512GB", "512Gb"),
        ("OTHER", "Other"),
    )

    PHONE_CONDITION = (
        ("NEW", "New"),
        ("USED", "Used"),
    )

    listing_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)
    listing_title = models.CharField(max_length=30)
    listing_description = models.TextField(max_length=300)
    listing_make = models.CharField(choices=PHONE_MAKE, default="OTHER", max_length=20)
    listing_model = models.CharField(max_length=20)
    listing_color = models.CharField(max_length=30)
    listing_internal_memory = models.CharField(choices=PHONE_INTERNAL_MEMORY, default="OTHER", max_length=20)
    listing_ram = models.CharField(choices=PHONE_RAM_MEMORY, default="OTHER", max_length=20)
    listing_condition = models.CharField(choices=PHONE_CONDITION, default="USED", max_length=20)
    listing_price = models.IntegerField()
    listing_image = models.ImageField(null=True, blank=True, upload_to="images/listing/")

    def __str__(self):
        return self.listing_title + " " + self.listing_price.__str__()


class Order(models.Model):
    order_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)
    order_listing = models.ForeignKey(MobileListing, on_delete=models.CASCADE)
    order_on_name = models.CharField(max_length=30)
    order_on_surname = models.CharField(max_length=40)
    order_on_city = models.CharField(max_length=40)
    order_on_municipality = models.CharField(max_length=40)
    order_delivery_address = models.CharField(max_length=30)
    order_delivery_address1 = models.CharField(max_length=30)
    order_phone_number = models.CharField(max_length=9)
    order_cc_number = models.CharField(max_length=16)
    order_cc_holder = models.CharField(max_length=40)
    order_cc_date = models.CharField(max_length=5)
    order_cc_cvv = models.CharField(max_length=3)

    def __str__(self):
        self.order_on_name + " " + self.order_listing.__str__()

