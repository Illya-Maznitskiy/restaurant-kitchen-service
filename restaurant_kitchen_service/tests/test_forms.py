from django.test import TestCase

from restaurant_kitchen.forms import CookCreationForm


class FormsTest(TestCase):
    def test_cook_creation_form_with_years_first_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "first_name": "new_first_name",
            "last_name": "new_last_name",
            "email": "new_email@mail.com",
            "years_of_experience": 7,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
