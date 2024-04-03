from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(
        null=True, blank=True, default=0, validators=[MaxValueValidator(99)])

    def get_absolute_url(self):
        return reverse(
            "restaurant_kitchen:cook-detail", kwargs={"pk": self.pk}
        )


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook)
