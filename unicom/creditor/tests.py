from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase, APIRequestFactory

from .models import Credit, Creditor
from partner.models import ApplicationForCreditor, Client
from .views import ApplicationReadOnlyView

now = datetime.now()


def create_models():
    creditor = Creditor(name='creditor')
    creditor.save()
    credit = Credit(rotation_start=now,
                    rotation_end=now,
                    name='credit',
                    credit_type='any',
                    score_min=1,
                    score_max=2,
                    creditor=creditor)
    credit.save()
    return credit, creditor


class TestModels(TestCase):
    def setUp(self):
        self.credit, self.creditor = create_models()

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


class TestViews(APITestCase):
    def setUp(self):
        self.credit, _ = create_models()
        now = datetime.now()
        self.client = Client(name='name', surname='surname', birth_date=now,
                             phone='111', passport='111', credit_score=1)
        self.client.save()

    def test_application_changes_status(self):
        app = ApplicationForCreditor(client=self.client, requested_credit=self.credit)
        app.save()
        self.assertEquals(app.status, ApplicationForCreditor.NEW)

        factory = APIRequestFactory()
        request = factory.get('/api/v1/partner/application')
        view = ApplicationReadOnlyView.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        app.refresh_from_db()
        self.assertEquals(app.status, ApplicationForCreditor.RECEIVED)
