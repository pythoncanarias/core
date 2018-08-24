from django.db import models


class Social(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=16, unique=True)
    base_url = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Speaker(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    bio = models.TextField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    photo = models.ImageField(
        upload_to='speakers/speaker/',
        blank=True
    )

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class Contact(models.Model):
    social = models.ForeignKey(
        Social,
        on_delete=models.PROTECT,
        related_name='contacts'
    )
    speaker = models.ForeignKey(
        Speaker,
        on_delete=models.PROTECT,
        related_name='contacts'
    )
    identifier = models.CharField(max_length=128)

    def __str__(self):
        return self.identifier
