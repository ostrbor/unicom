from django.db import models


class Creditor(models.Model):
    name = models.CharField(max_length=200)


class Credit(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    rotation_start = models.DateTimeField()
    rotation_end = models.DateTimeField()
    name = models.CharField(max_length=200)
    # TODO: add choices
    credit_type = models.CharField(max_length=100)
    # TODO: add validation - min<max
    # TODO: maybe replace scores with PositiveIntegerField
    score_min = models.IntegerField()
    score_max = models.IntegerField()
    creditor = models.ForeignKey(Creditor, on_delete=models.CASCADE)
