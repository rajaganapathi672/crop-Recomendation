import os

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'

# App settings
DEBUG = True