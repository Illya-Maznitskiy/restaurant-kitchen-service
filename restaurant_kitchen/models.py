from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(0),
        ]
    )

    def get_absolute_url(self):
        return reverse(
            "restaurant_kitchen:cook-detail", kwargs={"pk": self.pk}
        )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
        ],
        error_messages={
            "max_digits": "Price must have no more than 5 digits in total.",
            "max_decimal_places": "Price must have at most 2 decimal places.",
        }
    )
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
