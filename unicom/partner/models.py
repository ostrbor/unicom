from django.db import models

from unicom.creditor.models import Credit


class Client(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthdate = models.DateField()
    phone = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    # TODO: maybe replace with PositiveIntegerField
    credit_score = models.IntegerField()


class ApplicationForCreditor(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    requested_credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
    # TODO: replace with Choices
    status = models.CharField(max_length=50)
