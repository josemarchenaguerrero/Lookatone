@echo off
title Migrar Base de Datos

echo Creando migraciones...
python manage.py makemigrations
pause

echo Migrando...
python manage.py migrate
pause