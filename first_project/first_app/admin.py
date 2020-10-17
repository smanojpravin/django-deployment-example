from django.contrib import admin

from first_app.models import Topic,Webpage,AccessRecord,AppUser,UserProfileInfo

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(AppUser)
admin.site.register(UserProfileInfo)


# Register your models here.
