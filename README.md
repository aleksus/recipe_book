# Recipe Book

A Django web application for organizing recipes and connecting them with the cooks who share them. Browse and search recipes, ingredients, categories, and cooks; manage recipe details and ingredients; and leave a 1–5 rating and comment on a recipe.

## Requirements

- Python 3.13
- Dependencies listed in `requirements.txt`

## Set up locally

Run these commands from the project root. On Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the application.

To create an administrator account for the Django admin site, run:

```powershell
python manage.py createsuperuser
```

The development server and admin site are intended for local development, not production deployment.

## Demo data

Populate the database with sample recipes, cooks, ingredients, categories, and reviews:

```powershell
python manage.py seed_demo_data
```

The command is safe to run more than once; it creates or updates the included demo records.

## Features

- **Recipes:** create, view, update, delete, and search recipes; add ingredients and quantities.
- **Reviews:** add, edit, and delete reviews from a recipe page. Each cook can review a recipe once, with a rating from 1 to 5 and an optional comment.
- **Cooks:** browse and search cook profiles, view their reviews, and manage their profile details.
- **Ingredients and categories:** browse, search, and manage ingredients and recipe categories.
- **Dashboard:** see collection totals, recent recipes, recent cooks, and links to the main sections.

## Application structure

- `recipe_book/` — Django project settings and root URL configuration.
- `recipes/` — recipes, categories, ingredients, and recipe-ingredient relationships.
- `cooks/` — cook profiles.
- `reviews/` — recipe reviews and rating validation.
- `common/` — dashboard view.
- `templates/` — shared and app-specific HTML templates.

The project uses SQLite by default. Apply any pending schema changes with:

```powershell
python manage.py migrate
```