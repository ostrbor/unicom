from django.db import models
from django.utils.translation import gettext as _

from creditor.models import Credit


class Client(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    # TODO: maybe replace with PositiveIntegerField
    credit_score = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.surname


class ApplicationForCreditor(models.Model):
    NEW = 'New'
    SENT = 'Sent'
    RECEIVED = 'Received'

    status_choices = [
        (NEW, _('New status')),
        (SENT, _('Sent status')),
        (RECEIVED, _('Was viewed'))
    ]

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    requested_credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
    status = models.CharField(choices=status_choices, max_length=50, default=NEW)

    def __str__(self):
        return 'From client ' + self.client.surname + ' with status ' + self.status
