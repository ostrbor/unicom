from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Credit, Creditor

now = datetime.now()


class TestModels(TestCase):
    def setUp(self):
        self.creditor = Creditor.objects.create(name='creditor')
        Credit.objects.create(rotation_start=now,
                              rotation_end=now,
                              name='credit',
                              credit_type='any',
                              score_min=1,
                              score_max=2,
                              creditor=self.creditor)

    def test_credit_can_be_saved_with_any_credit_type(self):
        credit = Credit.objects.get(name='credit')
        self.assertNotIn(credit.credit_type, credit.credit_type_choices)

    def test_credit_raises_if_max_score_lt_min_score_with_save(self):
        with self.assertRaises(ValidationError):
            credit = Credit(rotation_start=now,
                            rotation_end=now,
                            name='credit',
                            credit_type='any',
                            score_min=2,
                            score_max=1,
                            creditor=self.creditor)
            credit.save()

    def test_credit_not_raises_if_max_score_lt_min_score_with_create(self):
        try:
            Credit.objects.create(rotation_start=now,
                                  rotation_end=now,
                                  name='credit',
                                  credit_type='any',
                                  score_min=1,
                                  score_max=2,
                                  creditor=self.creditor)
        except ValidationError:
            self.fail()
