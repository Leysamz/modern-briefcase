from django.test import TestCase
from organisations.models import Organisation

class OrganisationModelTest(TestCase):
    def test_create_organisation(self):
        organisation = Organisation.objects.create(
            name="Test Business",
            email="business@example.com",
        )

        self.assertEqual(organisation.name, "Test Business")
        self.assertEqual(organisation.email, "business@example.com")
        self.assertIsNotNone(organisation.created_at)

    def test_organisation_string_representation(self):
        organisation = Organisation.objects.create(
            name="Example Shop",
            email="shop@example.com",
        )
        self.assertEqual(str(organisation), "Example Shop")