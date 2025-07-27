from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.ifsc}"

