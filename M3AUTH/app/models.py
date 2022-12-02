from django.db import models

class Ambassador(models.Model):
    name= models.CharField(max_length=200,null=True)
    phone= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    skill= models.CharField(max_length=1,null=True)

    # name
    def __str__(self):
        return self.name

class Job(models.Model):
    CATEGORY = (
        ("Video","Video" ),
        ("Native","Native" ),
        ("Mobile","Mobile" ),
        ("Display","Display" ),

    )
    job_name= models.CharField(max_length=200,null=True)
    pay= models.FloatField(null=True)
    category= models.CharField(max_length=200,null=True, choices=CATEGORY)
    job_description= models.CharField(max_length=200,null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True,null=True)
    job_id= models.IntegerField(null=True)

    def __str__(self):
        return self.job_name

class Order(models.Model): #this is the in between first view of job and completion
    STATUS = (
        ("Recently Received","Recently Received" ),
        ("Working", "Working"),
        ("Awaiting Instructions","Awaiting Instructions"),
        ("Finished", "Finished"),

    )
    ambassador = models.ForeignKey(Ambassador, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL) 
    date= models.DateTimeField(auto_now_add=True,null=True)
    status= models.CharField(max_length=200,null=True, choices=STATUS)

    def __str__(self):
        return self.status