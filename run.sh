if [ ! -d "venv" ];
then
    python3.9 -m venv venv
    venv/bin/python -m pip install --upgrade pip
fi
venv/bin/python -m pip install --no-cache-dir -r requirements.txt
venv/bin/python manage.py collectstatic
venv/bin/python manage.py makemigrations
venv/bin/python manage.py migrate
venv/bin/uwsgi app.ini
