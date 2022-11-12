from django.test import TestCase

from taxi.forms import DriverCreationForm, validate_license_number


class FormsTests(TestCase):
    def test_driver_creation_form_with_license_number_first_name_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user1234",
            "password2": "user1234",
            "first_name": "Test first",
            "last_name": "Test last",
            "license_number": "DUS25131"
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_license_number_validation(self):
        self.assertEqual(validate_license_number("ABC12345"), "ABC12345")
        self.assertRegex(validate_license_number("ABC12345"), "^[A-Z]{3}\d{5}$")
