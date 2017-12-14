from django.db import models
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


class Creditor(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class Credit(models.Model):
    CONSUMER = 'CONS'
    MORTGAGE = 'MORT'
    AUTOLOAN = 'AUTO'
    BUSINESS = 'BUSI'

    credit_type_choices = [
        (CONSUMER, _('Потребительский')),
        (MORTGAGE, _('Ипотека')),
        (AUTOLOAN, _('Автокредит')),
        (BUSINESS, _('КМСБ'))
    ]

    created = models.DateField(auto_now_add=True, blank=False)
    updated = models.DateField(auto_now=True, blank=False)
    rotation_start = models.DateTimeField()
    rotation_end = models.DateTimeField()
    name = models.CharField(max_length=200)
    # TODO: restrict credit_types with Foreign Key constraint
    credit_type = models.CharField(choices=credit_type_choices, max_length=100)
    # TODO: maybe replace scores with PositiveIntegerField
    score_min = models.IntegerField()
    score_max = models.IntegerField()
    creditor = models.ForeignKey(Creditor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' from ' + self.creditor.name

    def clean(self):
        if self.score_max < self.score_min:
            raise ValidationError(_('Maxmum score is lesser than minimum credit score'))

    def save(self, *args, **kwargs):
        # TODO: model cleaning can be avoided with create. Add validation in forms.
        self.clean()
        super().save(*args, **kwargs)
