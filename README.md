# Prism Tech BE Test

## Prerequisites

-   Python 3.10.7
-   venv (virtual environment)

## Setup
* At PrismTechBETest folder:
  -   Create venv in backend directory:
      -   "python -m venv venv"
  -   Activate venv:
      -   "cd venv/scripts"
      -   "activate"
  -   Install library:
      -   "pip install -r requirements.txt"
  -   Migrate:
      -   "python manage.py migrate"
  -   Runserver: Server will run at port 8000
      -   "python manage.py runserver"

## Run API
* Generate sample data: At terminal, run "python manage.py generate_data"
* List APIs:
    - POST localhost:8000/api/user-auth/registration/ : Sign up new user
    - POST localhost:8000/api/user-auth/token/ : Login for an account, api will response a token
    - POST localhost:8000/api/product/create/ : Create new product with 3 infomation (name, quantity, description)
    - GET localhost:8000/api/product/ : List all products data
    - DELETE localhost:8000/api/product/<product_id>/ : Delete a product by <product_id>
* Testcase:
    - localhost:8000/api/user-auth/registration/
        - POST data: <br>
        { <br>
                &nbsp;&nbsp;&nbsp; "username": "emily_johnson", <br>
                &nbsp;&nbsp;&nbsp; "password1": "emily", <br>
                &nbsp;&nbsp;&nbsp; "password2": "emily" <br>
        }
    - localhost:8000/api/user-auth/token/
        - POST data: <br>
        { <br>
              &nbsp;&nbsp;&nbsp; "username": "dwayne_johnson", <br>
              &nbsp;&nbsp;&nbsp; "password": "dwayne", <br>
        }
    - localhost:8000/api/product/create/
        - POST data: <br>
        { <br>
                &nbsp;&nbsp;&nbsp; "name": "EcoFresh Air Purifier", <br>
                &nbsp;&nbsp;&nbsp; "quantity": "2", <br>
                &nbsp;&nbsp;&nbsp; "description": "EcoFresh Air Purifier description" <br>
        }