# Celery


## Installation of RabbitMQ
```bash
apt-get update
apt-get install rabbitmq-server
```

If you use another os: [RabbitMQ Installation for Other Distribution](https://www.rabbitmq.com/download.html)<br />
Additional document: [Install and Manage RabbitMQ](https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-rabbitmq)


## How to Run Celery
```bash
celery worker -A doit
```

**If you want to see your tasks list or output status**:
```bash
celery worker -A doit -l info
```

For further information of installation or running Celery: [First Steps With Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
