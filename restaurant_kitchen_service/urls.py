"""
URL configuration for restaurant_kitchen_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from restaurant_kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    toggle_assign_to_dish,
)


urlpatterns = [
    path("", index, name="index"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path("dishtypes/", DishTypeListView.as_view(), name="dishtype-list"),
    path(
        "dishtypes/create/",
        DishTypeCreateView.as_view(),
        name="dishtype-create"
    ),
    path(
        "dishtypes/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dishtype-update"
    ),
    path(
        "dishtypes/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dishtype-delete"
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dishes/<int:pk>/toggle-assign-cook/",
        toggle_assign_to_dish,
        name="toggle-assign-cook-to-dish"
    ),
]

app_name = "kitchen"
