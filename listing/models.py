from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    #status = models.CharField(max_length=200,help_text="Current Task Status")
    #completion_date = models.DateField(default=timezone.now())
    def __str__(self):
        return self.name

class Listing(models.Model):
    address = models.CharField(max_length=200, help_text="Property Address")
    price = models.IntegerField(help_text="Accepted Price",blank=True, default=0)
    physical_cr = models.CharField(max_length=200,blank=True, default='')
    appraisal_cr = models.CharField(max_length=200,blank=True, default='')
    loan_cr = models.CharField(max_length=200,blank=True, default='')
    coe = models.CharField(max_length=200, blank=True, default='')
    seller_name = models.CharField(max_length=200, blank=True, default='')
    buyer_name = models.CharField(max_length=200, blank=True, default='')
    listing_broker_name = models.CharField(max_length=200, blank=True, default='')
    escrow = models.IntegerField(blank=True,default=0)
    title = models.CharField(max_length=200, blank=True, default='')
    lender = models.CharField(max_length=200,blank=True, default='')
    hoa_name = models.CharField(max_length=200,blank=True,default='')
    vendors = models.ManyToManyField(Vendor,blank=True,default='')
    current_task = models.ForeignKey(Task, default=0, on_delete=models.CASCADE)
    def __str__(self):
        return self.address
