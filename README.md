# Crud simples usando Django Ninja e AlpineJs



## Este projeto foi feito com:

* [Python 3.11.3](https://www.python.org/)
* [Django 4.2.4](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [AlpineJs](https://alpinejs.dev/)

## Como rodar o projeto?

* Clone esse repositório.
* Instale o Poetry
* Crie um virtualenv com Poetry
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone git@github.com:djwesleyborges/django_djangoninja_alpinejs_crud.git
cd django_djangoninja_alpinejs_crud
pip install poetry
poetry install
poetry shell
python contrib/env_gen.py
python manage.py runserver

# Django local
python manage.py migrate
python manage.py createsuperuser --email="admin@email.com"
python manage.py runserver
```
