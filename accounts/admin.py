from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from accounts.models import ObjectPermission

class ObjectPermissionInline(GenericTabularInline):
    model = ObjectPermission
    raw_id_fields = ['user']
    ct_fk_field = 'object_pk'
    extra = 2

class ObjectPermissionMixin(object):
    def has_change_permission(self, request, obj=None):
        opts = self.opts
        return request.user.has_perm(opts.app_label + '.' +
                                     opts.get_change_permission(), obj)

    def has_delete_permission(self, request, obj=None):
        opts = self.opts
        return request.user.has_perm(opts.app_label + '.' +
                                     opts.get_delete_permission(), obj)

