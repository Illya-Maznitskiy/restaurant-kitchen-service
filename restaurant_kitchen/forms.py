from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from restaurant_kitchen.models import Cook, DishType, Dish


common_attrs = {"style": "background-color: white; width: 700px"}


class DishCreationForm(forms.ModelForm):
    dish_type = forms.ModelChoiceField(
        queryset=DishType.objects.all(),
        empty_label="",
        widget=forms.Select(attrs=common_attrs)
    )

    class Meta:
        model = Dish
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs=common_attrs),
            "description": forms.Textarea(attrs={'rows': 4, **common_attrs}),
            "price": forms.NumberInput(attrs=common_attrs),
            "cooks": forms.CheckboxSelectMultiple(attrs=common_attrs),
        }

    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
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


class DishUpdateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs=common_attrs),
            "description": forms.Textarea(attrs={'rows': 4, **common_attrs}),
            "price": forms.NumberInput(attrs=common_attrs),
            "dish_type": forms.Select(attrs=common_attrs),
            "cooks": forms.CheckboxSelectMultiple(attrs=common_attrs),
        }

    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class CookCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs=common_attrs),
        help_text=UserCreationForm.base_fields['password1'].help_text
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs=common_attrs),
        help_text=UserCreationForm.base_fields['password2'].help_text
    )

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )

        widgets = {
            "username": forms.TextInput(attrs=common_attrs),
            "first_name": forms.TextInput(attrs=common_attrs),
            "last_name": forms.TextInput(attrs=common_attrs),
            "email": forms.EmailInput(attrs=common_attrs),
            "years_of_experience": forms.TextInput(attrs=common_attrs),
        }


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )

        widgets = {
            "username": forms.TextInput(attrs=common_attrs),
            "first_name": forms.TextInput(attrs=common_attrs),
            "last_name": forms.TextInput(attrs=common_attrs),
            "email": forms.EmailInput(attrs=common_attrs),
            "years_of_experience": forms.TextInput(attrs=common_attrs),
        }

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("years_of_experience")
        if years_of_experience < 0:
            raise forms.ValidationError(
                "Years of experience cannot be negative"
            )
        return years_of_experience


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


class DishTypeCreationForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class DishTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


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
