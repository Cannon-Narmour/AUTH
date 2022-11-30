from django.db import models

class Customer(models.Model):
    name= models.CharField(max_length=200,null=True)
    phone= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    date= models.DateTimeField(auto_now_add=True,null=True)

    # name
    def __str__(self):
        return self.name

class Job(models.Model):
    CATEGORY = (
        ("Accepted","Accepted" ),
        ("Declined","Declined" ),
    )
    name= models.CharField(max_length=200,null=True)
    price= models.FloatField(null=True)
    category= models.CharField(max_length=200,null=True, choices=CATEGORY)
    job_description= models.CharField(max_length=200,null=True, blank=True)
    date= models.DateTimeField(auto_now_add=True,null=True)

    def str(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ("Recently Received","Recently Received" ),
        ("Working", "Working"),
        ("Awaiting Instructions","Awaiting Instructions"),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL) 
    date= models.DateTimeField(auto_now_add=True,null=True)
    status= models.CharField(max_length=200,null=True, choices=STATUS)

    def str(self):
        return self.job.name