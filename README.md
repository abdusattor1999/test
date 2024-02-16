Клонируйте репозиторий:
git clone https://github.com/abdusattor1999/test.git

Докер:
Постройте образ Docker:
    docker-compose up --build

API будет доступен по адресу http://localhost:5555
API endpoints:
    Пользователи:
        /user/ - список пользователей
        /user/<id>/ - информация о пользователе
    Блоги:
        /blog/ - список блогов
        /blog/<id>/ - информация о блоге
        /blog/<id>/subscribe - подписаться na блога     # authentication required
        /blog/<id>/unsubscribe - отписаться от блога    # authentication required
    Посты:
        /blog/post/ - новости из блогов, на которые подписаны
        /blog/post?blog=<id>/ - список постов в блоге
        /blog/post/<id>/ - информация о посте
        /blog/post/<id>/mark_as_watched/ - пометить как просмотренное
    

    Пример использования:
        GET http://localhost:5555/blog/
        # Ответ:
        [
            {
                "id": 1,
                "name": "user",
                "desctiption": null,
                "created_at": "2024-02-16T05:17:13.164900Z",
                "user": 5
            },
            {
                "id": 2,
                "name": "user1122",
                "desctiption": null,
                "created_at": "2024-02-16T08:10:33.164320Z",
                "user": 4
            }
        ]
