# Import the model classes we just wrote.

from django.utils import timezone
q = Question(title="What's new?", pub_date=timezone.now(),desc='fijsdfjkf', featured=False)
q.save()
