from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_first_name = models.CharField(max_length=50, verbose_name="Име")
    profile_last_name = models.CharField(max_length=50,  verbose_name="Презиме")
    profile_date_of_birth = models.DateField(verbose_name="Дата на раѓање")
    profile_phone_number = models.CharField(max_length=9, verbose_name="Телефонски број")
    profile_email = models.EmailField(verbose_name="Е-маил")
    profile_password = models.CharField(max_length=70, verbose_name="Лозинка")
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    profile_image = models.ImageField(upload_to="images/profile/", null=True, blank=True, verbose_name="Слика")

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
        ("OTHER", "Останато")
    )

    PHONE_RAM_MEMORY = (
        ("1GB", "1Gb"),
        ("2GB", "2Gb"),
        ("3GB", "3Gb"),
        ("4GB", "4Gb"),
        ("6GB", "6Gb"),
        ("8GB", "8Gb"),
        ("12GB", "12Gb"),
        ("OTHER", "Останато"),
    )

    PHONE_INTERNAL_MEMORY = (
        ("8GB", "8Gb"),
        ("16GB", "16Gb"),
        ("32GB", "32Gb"),
        ("64GB", "64Gb"),
        ("128GB", "128Gb"),
        ("256GB", "256Gb"),
        ("512GB", "512Gb"),
        ("OTHER", "Останато"),
    )

    PHONE_CONDITION = (
        ("NEW", "Користен"),
        ("USED", "Нов"),
    )

    listing_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)
    listing_title = models.CharField(max_length=30, verbose_name="Наслов")
    listing_description = models.TextField(max_length=300, verbose_name="Опис")
    listing_make = models.CharField(choices=PHONE_MAKE, default="OTHER", max_length=20, verbose_name="Марка")
    listing_model = models.CharField(max_length=20, verbose_name="Модел")
    listing_color = models.CharField(max_length=30, verbose_name="Боја")
    listing_internal_memory = models.CharField(choices=PHONE_INTERNAL_MEMORY, default="OTHER", max_length=20, verbose_name="Внатрешна меморија")
    listing_ram = models.CharField(choices=PHONE_RAM_MEMORY, default="OTHER", max_length=20, verbose_name="РАМ меморија")
    listing_condition = models.CharField(choices=PHONE_CONDITION, default="USED", max_length=20, verbose_name="Состојба")
    listing_price = models.IntegerField(verbose_name="Цена")
    listing_image = models.ImageField(null=True, blank=True, upload_to="images/listing/", verbose_name="Слика")

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

