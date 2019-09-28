#https://docs.djangoproject.com/en/1.11/topics/signals/#post-save
from django.db.models.signals import post_save
from .models import Request

from django.dispatch import receiver
from .models import Request

@receiver(post_save, sender=Request)
def send_request_email(sender, **kwargs): 
	i = kwargs['instance']
	request = Request.objects.get(id=i.id)
	request.send_request_email( i.get_email_to() )

