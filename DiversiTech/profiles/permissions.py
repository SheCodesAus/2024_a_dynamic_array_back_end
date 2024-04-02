from rest_framework import permissions

class IsOwnerOrAdminOrReadOnly(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: 
            return True
        
        if request.user.is_staff:
            return True

        return obj.owner==request.user
    
class IsProfileOwnerOrAdminOrReadOnly(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj):
        profile_id = obj.profile.owner.id
 
        if request.method in permissions.SAFE_METHODS: 
            return True
        
        if request.user.is_staff:
            return True
        print(profile_id)
        print(request.user.id)
        return profile_id==request.user.id