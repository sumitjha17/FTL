from django.db import models
from django.urls import reverse



class Activity_period(models.Model):

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    member_id= models.ForeignKey('Members', on_delete=models.SET_NULL, null=True) 
	
    def __str__(self):
        """String for representing the Model object."""
        return self.member_id
		
	
	



class Members(models.Model):
    """Model representing a users """
    real_name =   models.CharField(max_length=200)
    address =     models.CharField(max_length=200)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.real_name
    
    class Meta:
        ordering = ['real_name']
