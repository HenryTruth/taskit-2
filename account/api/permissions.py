from rest_framework import permissions

class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs

    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted

class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are already authenticated. Please log out to try again'
    """
    Global permission check for blacklisted IPs

    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'you must be the owner of this content to change it'
    """
    Object-level permmissions to only allow of an object to edit it.
    Assume the model instance has an owner attribute.

    """

    def has_object_permission(self, request, view, obj):
        # Read permission are allowed to any request
        # so we' ll always allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute name 'owner'
        return obj.owner == request.user