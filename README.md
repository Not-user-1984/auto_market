#### Авто - католог:

запуск
```
git clone git@github.com:Not-user-1984/avto_market.git

python -m venv 
source venv/bin/activate 
pip install -r requirements.txt 

cd src
python manage.py migrate 
python manage.py runserver 
```
есть два теста которые проверяют парсер и обновления базы. 

````
cd src

pytest
````
