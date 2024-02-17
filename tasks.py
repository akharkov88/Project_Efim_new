
from celery import Celery
import telebot



celery=Celery("task",broker='redis://localhost:6379')
@celery.task
def add(x, y):
    return x + y

def some_other_foo(value):
    raise Exception('This is not handled!')
    # print(123)

@celery.task(
  bind=True,
  max_retries=5,
  soft_time_limit=20)
def some_foo(self):
    response = ""

    try:
        response = some_other_foo('test')
    except Exception as exc:
        self.retry(countdown=5, exc=exc)
        response = "error"

    return response

@celery.task(name="Оправка сообщений")
def send_message(id ,data):
    bot = telebot.TeleBot('6699554023:AAFv2VuN2NcqydlFlkK5qCpLmCzLL3Euy_g')
    bot.send_message(id, data)
    # print(123)
    return True