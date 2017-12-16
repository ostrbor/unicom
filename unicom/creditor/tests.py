from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase, APIRequestFactory

from .models import Credit, Creditor
from partner.models import ApplicationForCreditor, Client
from .views import ApplicationReadOnlyView
from unicom.settings import CREDITOR_GROUP, ADMIN_GROUP, PARTNER_GROUP

now = datetime.now()
factory = APIRequestFactory()


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
    # TODO: refactor tests
    def setUp(self):
        self.credit, _ = create_models()
        now = datetime.now()
        self.client = Client(name='name', surname='surname', birth_date=now,
                             phone='111', passport='111', credit_score=1)
        self.client.save()
        self.app = ApplicationForCreditor(client=self.client, requested_credit=self.credit)
        self.app.save()

    def test_application_changes_status(self):
        creditor_user = User.objects.create_user('creditor', password='creditor')
        creditor_user.save()

        creditor_group = Group(name=CREDITOR_GROUP)
        creditor_group.save()
        creditor_user.groups.add(creditor_group)

        self.assertEquals(self.app.status, ApplicationForCreditor.NEW)

        request = factory.get('/api/v1/partner/application')
        request.user = creditor_user
        view = ApplicationReadOnlyView.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        self.app.refresh_from_db()
        self.assertEquals(self.app.status, ApplicationForCreditor.RECEIVED)

    def test_creditor_and_admin_has_perm_to_application_view(self):
        creditor_user = User.objects.create_user('creditor', password='creditor')
        creditor_user.save()

        creditor_group = Group(name=CREDITOR_GROUP)
        creditor_group.save()
        creditor_user.groups.add(creditor_group)

        request = factory.get('/api/v1/partner/application')
        request.user = creditor_user
        view = ApplicationReadOnlyView.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        self.assertEquals(response.status_code, 200)

        creditor_user.groups.remove(creditor_group)
        admin_group = Group(name=ADMIN_GROUP)
        admin_group.save()
        creditor_user.groups.add(admin_group)

        request = factory.get('/api/v1/partner/application')
        request.user = creditor_user
        view = ApplicationReadOnlyView.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        self.assertEquals(response.status_code, 200)

    def test_partner_and_anon_has_no_perm_to_application_view(self):
        request = factory.get('/api/v1/partner/application')
        view = ApplicationReadOnlyView.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        self.assertEquals(response.status_code, 403)

        creditor_user = User.objects.create_user('creditor', password='creditor')
        creditor_user.save()

        partner_group = Group(name=PARTNER_GROUP)
        partner_group.save()
        creditor_user.groups.add(partner_group)

        request = factory.get('/api/v1/partner/application')
        request.user = creditor_user
        view = ApplicationReadOnlyView.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        self.assertEquals(response.status_code, 403)
