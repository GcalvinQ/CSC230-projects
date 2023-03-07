from django.db import models

# Create your models here.
class Account(models.Model):
    firstname = models.CharField(db_column='firstName', primary_key=True, max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=44)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account'
        unique_together = (('firstname', 'lastname', 'email'),)
    
    def __str__(self):
        return self.username