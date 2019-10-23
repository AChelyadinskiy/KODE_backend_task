from celery import shared_task
import requests
from subscriptions.models import Subscription
from django.core.mail import send_mail


@shared_task
def check_subscriptions():
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=E5VTULXGP00PFBSD"
    mail_from = "chelyadinskiy.test@gmail.com"
    topic = "Изменения по котировкам"
    answer = "По тикеру {} цена перешла пороговое значение {} и на данный момент составляет {}"
    for sub in Subscription.objects.all():
        r = requests.get(url.format(sub.ticker)).json()
        price = float(r["Global Quote"]["05. price"])
        if sub.max_price is not None:
            if price > sub.max_price:
                send_mail(topic, answer.format(sub.ticker, sub.max_price, price), mail_from, [sub.email])
        if sub.min_price is not None:
            if price < sub.min_price:
                send_mail(topic, answer.format(sub.ticker, sub.min_price, price), mail_from, [sub.email])
    print("success")
