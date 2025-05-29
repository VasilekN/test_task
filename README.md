# Parse service

A Django-based web service that provides an API with endpoints to create pages, get pages by ID, and list pages with
optional ordering.

## Installation

Clone the repository:

```
git clone https://github.com/VasilekN/test_task.git
cd test_task
```

2. Configure project:

- Run docker compose. It will start automatic configuration of MySQL and Django backend, which will perform migrations and start itself.

```
$ docker compose up -d
```

- Stop and remove the containers

```
$ docker compose down
```

## Run the server

By default, the server will be available at:
http://127.0.0.1:8000

The Django admin site is activated by default. You can open a Web browser and go to “/admin/” on your local domain –
e.g., http://127.0.0.1:8000/admin/.
Try logging in with the superuser account which you created. You should see the Django admin index page.

