# Antropika landing page

## Installation
Instructions for setting up your project locally.

```bash
# Clone the repository


# Navigate into the project directory
cd antropika_landing_page

# Create a virtual environment
python -m venv venv

# Activate the environment
- bash: source ./venv/Scripts/activate
- powershell: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# SEED THE APP REQUIRED DATA
python manage.py seed_data

# RUN THE SERVER
python manage.py runserver


#For migration
python manage.py migrate 

## CREATE APP
cd ./apps
python ../manage.py startapp app_name
cd ..
