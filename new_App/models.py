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