# commands
cd ./sber \
pip install -r ./requirements.txt \
python manage.py makemigrations && python manage.py migrate \
загрузка тестовой бд \
python manage.py loaddata objects &&
python manage.py loaddata entrants &&
python manage.py loaddata directions

# P.S.
для получение списка предметов по определенному направлению
нужно ввести ссылку /objects_direction/uuid
где uuid, id направления