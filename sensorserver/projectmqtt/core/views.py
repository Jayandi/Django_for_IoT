from django.shortcuts import render, HttpResponse
from core.models import Messages
import sqlite3


def main_page(request):
    Messages_ = Messages.objects.all()
    return render(request, 'core/Main_page.html', {'Messages': Messages_})


def load(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    data = cursor.execute('SELECT message_id, message, topic, time FROM core_messages')
    text = '\n'.join(list(map(str, data)))
    return HttpResponse(text)
