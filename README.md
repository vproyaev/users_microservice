
Users Microservice
===========

### Доступные комманды API (примеры через консоль Linux)

1. Получить список всех пользователей в базе данных - GET запрос: curl -i http://127.0.0.1:80/users 
2. Удалить пользователя по id - DELETE запрос: curl -v -X DELETE http://127.0.0.1:80/users/1
3. Добавить пользователя - POST запрос: curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Vlad", "surname": "Vlad", "phone": "79990009900"}' http://127.0.0.1:80/users


Все данные передаются в JSON.

```
Что бы не ползать по репозиторию, все файлы, с которыми велась работа - доступны ниже.
```

Файлы:
 1. [Весь код тут](https://github.com/vproyaev/users_microservice/blob/master/main.py)

