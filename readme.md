# Calculator Django
## Membuat Calculator dengan Django
Struktur Folder
```
django-calculator
├───apps
│   └───__pycache__
└───math_apps
    ├───migrations
    │   └───__pycache__
    ├───static
    │   ├───css
    │   └───js
    ├───templates
    │   ├───partials
    │   └───views
    └───__pycache__
```
<hr />
list url yang tersedia:

- admin/
- math/
    - /
    - /calculator/

<hr />
Web ini menggunakan:

- <img src="math_apps/static/images/django.svg" width="48px" alt="Django icons" />
- <img src="math_apps/static/images/bootstrap.svg" width="48px" alt="Bootstrap icons" />
- <img src="math_apps/static/images/font-awesome.svg" width="48px" alt="Font Awesome icons" />
- <img src="math_apps/static/images/jquery-plain-wordmark.svg" width="48px" alt="JQuery icons" />


<hr />
Cara menggunakan

- Clone project ini menggunakan command ```git clone https://github.com/kamachiii/django-calculator```
- Buat virtual env ```python -m venv env```
- Gunakan virtual env

    PowerShell
    ```powershell
    ./env/Scripts/activate.ps1
    ```
    Git Bash
    ```git
    source ./env/Scripts/activate
    ```
- Install Django ```pip install django```
- Jalankan server ```python manage.py runserver```
