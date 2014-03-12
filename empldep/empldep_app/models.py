from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)