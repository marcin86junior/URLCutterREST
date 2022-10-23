from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings
from django.utils import timezone


class Link(models.Model):
    original_link=models.URLField()
    shortened_link=models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_time_used = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def shortener(self):
        while True:
            random_string=''.join(choices(ascii_letters,k=6))
            new_link=settings.HOST_URL+'/'+random_string
            if not Link.objects.filter(shortened_link=new_link).exists():
                break
        return new_link

    def save(self,*args, **kwargs):
        if not self.shortened_link:
            new_link=self.shortener()
            self.shortened_link=new_link
        return super().save(*args, **kwargs)

    def increase_short_id_counter(self) -> None:
        """When a user request a original url with the short_id."""
        self.count += 1
        self.last_time_used=timezone.now()
        self.save()

    def __str__(self):
        return self.original_link
