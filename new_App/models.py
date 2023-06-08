from django.db import models

# Create your models here.
class Master(models.Model):
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=50, default=str())
    IsActive=models.BooleanField(default=False)

    class Meta:
        db_table="master"

    def __str__(self) -> str:
        return self.Email
    

class Common(models.Model):
    Master=models.ForeignKey(Master, on_delete=models.CASCADE)
                                                                                   
    Name=models.CharField(max_length=50)
    DateOfBirth=models.DateField(default='2022-11-21')
    DateOfJoining=models.DateField(default='2022-11-21')
    Address=models.CharField(max_length=100)

    class Meta:
        db_table="common"

    def __str__(self) -> str:
        return self.Name if self.Name else self.Master.Email