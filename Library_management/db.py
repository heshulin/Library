from Library_management.models import BlackList, Subscribe, Record
import datetime, time


def run():
    while True:
        s = Subscribe.objects.filter().all()
        l = Record.objects.filter().all()
        for i in s:
            dt = datetime.datetime.now()
            if i.EndTime < dt:
                i.delete()
                i.save()
        for j in l:
            dt = datetime.datetime.now()
            if j.EndTime < dt:
                b = BlackList()
                b.UserId = j.UserId
                b.BookId = j.BookId
                b.save()
        time.sleep(43200)
