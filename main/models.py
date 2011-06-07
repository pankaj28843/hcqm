from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

class HealthCenterType(models.Model):
    '''
    This model is used to save different types of health centers.
    '''
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'), blank=True)

    def __unicode__(self):
        return '%s' %(self.name.title())

class HealthCenter(models.Model):
    '''
    Basic details about health center including lattitude and longitude.
    '''
    name = models.CharField(_('name'), max_length=100)
    type = models.ForeignKey(HealthCenterType)
    lattitude = models.FloatField(_('lattitude'))
    longitude = models.FloatField(_('longitude'))
    description = models.TextField(_('description'), blank=True)

    def __unicode__(self):
        return '%s' %(self.name.title())

class RatingCriteria(models.Model):
    name = models.CharField(_('name'), max_length=100)
    max_value = models.FloatField(_('maximum value'))
    min_value = models.FloatField(_('minimum value'))
    description = models.TextField(_('description'))

    def __unicode__(self):
        return '%s' %(self.name.title())

class Rating(models.Model):
    value = models.FloatField(_('value'))
    health_center = models.ForeignKey(HealthCenter)
    criteria = models.ForeignKey(RatingCriteria)
    date = models.DateTimeField(_('date'), auto_now_add=False)
    description = models.TextField(_('description'))

    def __unicode__(self):
        return 'Value-%f, Criteria-%s, Health Center-%s' %(self.value,
                self.criteria, self.health_center, self)

