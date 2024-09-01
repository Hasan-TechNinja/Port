from django.contrib import admin
from .models import Contact, Footer, Experience, About

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
    
admin.site.register(Contact, ContactAdmin)


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'url')

admin.site.register(Footer, FooterAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'company_name', 'location', 'start_date', 'end_date', 'is_current', 'description', 'technologies', 'company_logo', 'company_website')

admin.site.register(Experience, ExperienceAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'education', 'description', 'CV', 'image')

admin.site.register(About, AboutAdmin)