"# sber" 
установить библиотеки
сделать миграции
запустить фикстуры


# commands
git clone \
pip install -r ./requirements.txt \
python manage.py makemigrations && python manage.py migrate \
python manage.py loaddata objects &&
python manage.py loaddata entrants &&
python manage.py loaddata directions &&