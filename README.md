# Django Notes App

A simple and clean note-taking application built with Django and Bootstrap 5.

## Features

- Create, read, update, and delete notes
- Clean and responsive user interface
- Bootstrap 5 styling
- Flash messages for user feedback
- Automatic timestamps for creation and updates

## Tech Stack

- Django 5.2.4
- Bootstrap 5.3.0
- SQLite database
- Python 3.x

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd DjangoNotingApp
```

2. Create and activate virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:

```bash
pip install django
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

```
DjangoNotingApp/
├── notes/                  # Main app directory
│   ├── models.py          # Note model
│   ├── views.py           # View functions
│   ├── forms.py           # Forms for note creation/editing
│   ├── urls.py            # URL routing
│   └── templates/         # HTML templates
├── noting/                # Project settings
└── manage.py             # Django management script
```

## Usage

- Visit the homepage to see all notes
- Click "Create Note" to add a new note
- Each note card has "Edit" and "Delete" options
- Notes are automatically sorted by last update time

## Contributing

Feel free to fork the repository and submit pull requests.

## License

This project is open-source and available under the MIT License.
