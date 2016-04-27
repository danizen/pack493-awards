from django.db import models


class Den(models.Model):
    '''
    Each Den has a leader who is a user who may administrate the Den,
    a list of Scouts, and a list of potential Activities
    '''
    name = models.CharField(max_length=64, unique=True)


class Activity(models.Model):
    '''
    An Activity belongs to a Den. Each Activity may be required or an elective.
    '''
    name = models.CharField(max_length=64, unique=True)
    den = models.ForeignKey(Den, on_delete=models.CASCADE)
    required = models.BooleanField(default=False)


class Scout(models.Model):
    '''
    A Scout is a member of a Den, and earns Awards by performing Activities
    '''
    name = models.CharField(max_length=64, unique=True)
    den = models.ForeignKey(Den, on_delete=models.CASCADE)


class Award(models.Model):
    '''
    A scout earns awards. These awards are earned, reported, purchased, and
    delivered at particular times. Den masters mark the award as earned. The
    awards coordinator reports the award and purchases the award. Then the Den
    leaders deliver the award.
    '''
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    scout = models.OneToOneField(Scout, on_delete=models.CASCADE)
    earned = models.DateField(null=True)
    reported = models.DateField(null=True)
    purchased = models.DateField(null=True)
    delivered = models.DateField(null=True)

