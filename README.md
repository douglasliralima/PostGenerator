
# Django Project

This is a Django project that provides an API for various features. It uses **Pipenv** to manage dependencies and virtual environments.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Pip (Python package manager)
- Pipenv (Dependency manager for Python)

To install Pipenv, run:

```bash
pip install pipenv
```

Additionally, some Linux-specific dependencies need to be installed. Run the following:

```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install ttf-mscorefonts-installer
```

## Installation

Follow these steps to set up the project:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```

2. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

3. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

4. Apply Django migrations:
   ```bash
   python manage.py migrate
   ```

## Running the Project

1. Ensure the virtual environment is active:

   ```bash
   pipenv shell
   ```

2. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

## Troubleshooting

- If you encounter issues with missing dependencies, run:

  ```bash
  pipenv install
  ```

- To deactivate the virtual environment:
  ```bash
  exit
  ```
