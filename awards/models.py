from django.db import models
from django.conf import settings


class ReprMixin():
    
    def __repr__(self):
        return '<'+self.__class__.__name__+': '+self.name+'>'

    def __str__(self):
        return self.name


class DenManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)
         

class Den(ReprMixin, models.Model):
    '''
    Each Den has a leader who is a user who may administrate the Den,
    a list of Scouts, and a list of potential Adventures
    '''
    objects = DenManager()

    name = models.CharField(max_length=64, unique=True)
    leader = models.OneToOneField(
                settings.AUTH_USER_MODEL, 
                null=True, 
                on_delete=models.SET_NULL
            )

    def natural_key(self):
        return self.name


class Adventure(ReprMixin, models.Model):
    '''
    An Adventure belongs to a Den. Each Adventure may be required or optional.
    '''
    name = models.CharField(max_length=64, unique=True)
    den = models.ForeignKey(Den, on_delete=models.CASCADE)
    required = models.BooleanField(default=False)


class Scout(ReprMixin, models.Model):
    '''
    A Scout is a member of a Den, and earns Awards by having Adventures
    '''
    name = models.CharField(max_length=64, unique=True)
    den = models.ForeignKey(Den, on_delete=models.CASCADE, related_name='scouts')
    awards = models.ManyToManyField(Adventure,
                                    through='Award',
                                    through_fields=('scout', 'adventure'))


class Award(ReprMixin, models.Model):
    '''
    A scout earns Awards for completing Adventures. 
    These awards are earned, reported, purchased, and delivered.
    Den leaders mark the award as earned. 
    The awards coordinator reports the award and purchases the award. 
    Then the Den leaders deliver the award.
    '''
    scout = models.ForeignKey(Scout, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    earned = models.DateField(null=True)
    reported = models.DateField(null=True)
    purchased = models.DateField(null=True)
    delivered = models.DateField(null=True)

