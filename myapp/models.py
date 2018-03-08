from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.firstname, self.last_name)
