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

    def get_health_centers(self):
        return HealthCenter.objects.all().filter(type=self)

    def get_ratings(self):
        return Rating.objects.all().filter(health_center__type=self)

class HealthCenter(models.Model):
    '''
    Basic details about health center including lattitude and longitude.
    '''
    name = models.CharField(_('name'), max_length=100)
    type = models.ForeignKey(HealthCenterType)
    latitude = models.FloatField(_('latitude'))
    longitude = models.FloatField(_('longitude'))
    description = models.TextField(_('description'), blank=True)

    def __unicode__(self):
        return '%s' %(self.name.title())

    def get_rating(self, rc_id=0):
        try:
            rc = RatingCriteria.objects.get(id=rc_id)
            return Rating.objects.get(health_center=self, criteria=rc).value
        except:
            s = 0
            ratings = Rating.objects.all().filter(health_center=self)
            for r in ratings:
                s = s + r.value
            return s

class RatingCriteria(models.Model):
    name = models.CharField(_('name'), max_length=100)
    max_value = models.FloatField(_('maximum value'))
    min_value = models.FloatField(_('minimum value'), default=0)
    description = models.TextField(_('description'), blank=True)

    def __unicode__(self):
        return '%s' %(self.name.title())

class Rating(models.Model):
    value = models.FloatField(_('value'))
    health_center = models.ForeignKey(HealthCenter)
    criteria = models.ForeignKey(RatingCriteria)
    date = models.DateTimeField(_('date'), auto_now_add=False)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        unique_together = (('health_center', 'criteria'),)

    def __unicode__(self):
        return 'Value-%f, Criteria-%s, Health Center-%s' %(self.value,
                self.criteria, self.health_center)

