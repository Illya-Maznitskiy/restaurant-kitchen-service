from django import forms
from django.contrib.auth.forms import UserCreationForm

from restaurant_kitchen.models import Cook, DishType, Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("years_of_experience")
        if years_of_experience < 0:
            raise forms.ValidationError(
                "Years of experience cannot be negative"
            )
        return years_of_experience


class DishTypeCreationForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class DishTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class DishCreationForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class DishUpdateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
