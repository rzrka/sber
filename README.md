# commands
cd ./sber \
pip install -r ./requirements.txt \
python manage.py makemigrations && python manage.py migrate \
загрузка тестовой бд \
python manage.py loaddata objects &&
python manage.py loaddata entrants &&
python manage.py loaddata directions