from django.db import models


class TeamMember(models.Model):
    title = models.CharField('Name', max_length=20)
    role = models.CharField('Role', max_length=20)
    bio = models.CharField('About', max_length=50)
    imgUrl = models.URLField('Image URL')

    def __str__(self):
        return self.title
    