#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primerProyecto.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#para crear un proyecto django dirigir se al directorio C:\Users\Usuario\VisualCodeStudio\Python\django en Powershell y poner: django-admin startproject nombreproyecto
#para sincronizar la bbdd con el proyecto escribir en Powershell: python manage.py migrate -------- y se creará la base de datos de sqlite3
#para ejecutar el servidor por defecto de django escribir en Powershell: python manage.py runserver