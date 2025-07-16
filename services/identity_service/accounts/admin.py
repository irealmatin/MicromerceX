from django.contrib import admin , messages
from django.contrib.auth.admin import UserAdmin
from .models import User , UserProfile



class SellerApplicantFilter(admin.SimpleListFilter):
    """
    Admin filter for users with seller applications.
    """
    title = "seller application status"
    parameter_name = "is_seller_applicant"

    def lookups(self, request, model_admin):
        """Define available filter options.
        
        Returns:
            tuple: (value, human-readable label) pairs.
        """
        return (
            ('yes', 'Has Application'),
        )
    
    def queryset(self, request, queryset):
        """base on user choice , filter the queryset"""

        if self.value() == "yes" :
            #return that users who submited for seller applicant
            return queryset.filter(profile__is_seller_applicant=True)
        
        return queryset




@admin.action(description="Approve selected users as sellers")
def approve_as_seller(modeladmin, request, queryset):
    """Admin action to approve users as sellers.
    
    Args:
        modeladmin: ModelAdmin instance.
        request: HttpRequest object.
        queryset: Selected User objects to approve.
    """
    updated_count = queryset.update(role=User.Role.SELLER)

    #update field in profile
    user_ids = queryset.values_list('id' , flat = True)
    UserProfile.objects.filter(user_id__in=user_ids).update(is_seller_applicant=False)

    messages.success(request , f"{updated_count} user(s) were successfully approved as sellers.")
   

class CustomUserAdmin(UserAdmin):
    """
    Custom User admin interface with seller management features.
    """
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = (SellerApplicantFilter,'role', 'is_staff', 'is_superuser')
    actions = [approve_as_seller]

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )




try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)