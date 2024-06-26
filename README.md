# Restaurant Kitchen Service

## Description of the project:
This project aims to make the kitchen more efficient by helping cooks communicate better and follow clear rules.
It's like creating a system for organizing who cooks which dish, and it also allows them to easily create new dishes.
This system is designed to help everyone work together more effectively in the kitchen, reducing confusion and ensuring tasks are completed efficiently.

## Discover the kitchen system!
(Wait a minute for the server to load)

[Check it out! Restaurant Kitchen Service deployed on Render](https://restaurant-kitchen-service-9kz3.onrender.com/)

### Login Information

Use the following credentials to login:

- **Username:** user
- **Password:** user12345

## Technologies used:
In this project I used the following technologies:
  - Python
  - Django
  - HTML
  - CSS

## Installation:
To run the project locally on your computer, execute the following commands in a terminal:
```
git clone https://github.com/Illya-Maznitskiy/restaurant-kitchen-service.git
cd restaurant-kitchen-service
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py runserver
```

## Commands to test the project:
You can use the following commands to run written tests and check the code style using flake8:
```
python manage.py test
flake8
```

## Description main features:

- **Simple and User-Friendly Interface**:
  
  The system simplifies kitchen tasks with an easy-to-use interface, enabling quick creation and management of dish types, dishes and cooks.


- **Dish Management**:
  
  Manage dish types and individual dishes easily within the system. This feature makes cooking smoother by enabling the creation of new dishes and types, improving kitchen operations.


- **Cooks Management**:

  Simplify kitchen operations by managing cook information effectively. The system allows for the addition of cook details and assigns them to specific dishes, ensuring accurate records.

## Screenshots:
![Login](screenshots/restaurant_kitchen_login.jpg)
![Home Page](screenshots/restaurant_kitchen_home.jpg)
![Cook List](screenshots/restaurant_kitchen_cook_list.jpg)

## Database structure:
![DB_structure](https://media.mate.academy/Kitchen_Service_d1fcaa4cdb.png)
