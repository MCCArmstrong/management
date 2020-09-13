from datetime import date, datetime
from users.models import User
from django.db import models
from django.db.models import Avg
from django.contrib import messages
from .validator import ExtensionValidator

SERVICE_TITLE = [
    ('', 'Service Category'),
    ('Software Development', 'Software Development'),
    ('Software Security', 'Software Security'),
    ('Data Science', 'Data Visualization'),
    ('Software Training', 'Software Training'),
    ('Business Consultancy', 'Business Consultancy'),
]


class CustomerPurchaseForm(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    amount = models.FloatField()
    address = models.TextField(blank=True)

    def __str__(self):
        return self.email


class MakeRequest(models.Model):
    fullname = models.CharField(max_length=30, help_text='Indicate your fullname')
    mobile = models.PositiveSmallIntegerField(help_text='Please indicate your mobile number')
    businessname = models.CharField(max_length=20, help_text='Write your business name')
    business_category = models.CharField(max_length=30, choices=((x, x)
                                                                 for x in ['Corporation', 'Medium Enterprise',
                                                                           'Small Enterprise', 'Micro Enterprise']))

    def __str__(self):
        return self.business_category


class caviet(models.Model):
    sliders = models.ImageField(upload_to='image/slides')
    description = models.CharField(max_length=30, blank=True, null=True)
    preview = models.TextField(max_length=200)

    def __str__(self):
        return self.description


class unicornabout(models.Model):
    file = models.ImageField(upload_to='image/about')
    about = models.TextField(max_length=200)
    history = models.TextField(max_length=200)

    def __str__(self):
        return self.about


class unicornService(models.Model):
    service_title = models.CharField(max_length=40, choices=SERVICE_TITLE, default=None, help_text='Add Service Title')
    service_icon = models.FileField(upload_to='images/services/%Y/%m/')
    service_description = models.TextField(default=None, help_text='Write your service description here')

    class Meta:
        verbose_name = ['Services']

    def __str__(self):
        return self.service_title


class DailyTask(models.Model):
    task_name = models.TextField(max_length=20)
    task_description = models.CharField(max_length=150)
    task_date = models.DateField(default=date.today, blank=True)
    time_assigned = models.TimeField(auto_now=True, blank=True)
    time_completed = models.TimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.task_name


class ProductPortfolio(models.Model):
    product_name = models.CharField(max_length=50, default=None, help_text='Add a product name here')
    portfolio_file = models.ImageField(upload_to='images/portfolio', help_text='Add a photo of your portfolio here')
    product_description = models.CharField(max_length=80, help_text='Add your product description here..')
    product_price = models.IntegerField(help_text="Add a valid price here")
    date_created = models.DateTimeField(default=None, help_text="Add date of Software creation")

    @property
    def get_computed_rate(self):
        rating_average = self.productreviewrating_set.aggregate(average=Avg('rating_value'))
        # print(rating_average)

        if rating_average['average'] == None:
            return 0
        weighted_value = rating_average['average'] / 20
        # print("Final value >>>>>> ", weighted_value)
        return weighted_value


class ProductReviewRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductPortfolio, on_delete=models.CASCADE)
    rating_value = models.FloatField(default=0)
    review_note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review_rating = models.PositiveSmallIntegerField(help_text='Make integer rating here')
    review_text = models.TextField(max_length=100, help_text='Write a review here...')

    def __str__(self):
        return self.review_text
