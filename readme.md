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

- Django
- Bootstrap
- Font Awesome
- JQuery

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
