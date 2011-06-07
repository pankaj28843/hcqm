from django.db import models

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

class ObjectPermission(models.Model):
    user = models.ForeignKey(User)
    can_view = models.BooleanField()
    can_change = models.BooleanField()
    can_delete = models.BooleanField()

    content_type = models.ForeignKey(ContentType)
    object_pk = models.CharField(max_length=200)

    def __unicode__(self):
        obj = self.content_type.get_object_for_this_type(pk=self.object_pk)
        return 'Permission for %s on %s' %(self.user, obj)
