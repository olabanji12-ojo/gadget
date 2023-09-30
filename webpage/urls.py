from django.urls import path
from .import views

urlpatterns = [
    path("", views.main, name="main"),
    path("products/", views.products, name="products"),
    path("products/Laptop_to_choose/", views.Laptop_to_choose, name="Laptop_to_choose"),
    path("products/Phone_to_choose/", views.Phone_to_choose, name="Phone_to_choose"),
    path("products/Laptop_to_choose/Hplaptops/", views.Hplaptops, name="Hplaptops"),
    path("products/Laptop_to_choose/Dell_laptops/", views.Dell_laptops, name="Dell_laptops"),
    path("products/Laptop_to_choose/Toshiba_laptops/", views.Toshiba_laptops, name="Toshiba_laptops"),
    path("products/Phone_to_choose/Techno_phones/", views.Techno_phones, name="Techno_phones"),
    path("products/Phone_to_choose/Redmi_phones/", views.Redmi_phones, name="Redmi_phones"),
    path("products/Phone_to_choose/Infinix_phones/", views.Infinix_phones, name="Infinix_phones"),
    path("products/Laptop_to_choose/Hplaptops/Hpdetails/<int:id>", views.Hpdetails, name="Hpdetails"),
    path("products/Laptop_to_choose/Dell_laptops/Dell_details/<int:id>", views.Dell_details, name="Dell_details"),
    path("products/Laptop_to_choose/Toshiba_laptops/Toshiba_details/<int:id>", views.Toshiba_details, name="Toshiba_details"),
    path("products/Phone_to_choose/Techno_phones/Techno_details/<int:id>", views.Techno_details, name="Techno_details"),
    path("products/Phone_to_choose/Redmi_phones/Redmi_details/<int:id>", views.Redmi_details, name="Redmi_details"),
    path("products/Phone_to_choose/Infinix_phones/Infinix_details/<int:id>", views.Infinix_details, name="Infinix_details"),
]
