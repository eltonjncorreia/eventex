from django.contrib import admin

# Register your models here.
from eventex.core.models import Speaker, Contact, Talk


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'


    def photo_img(self, obj):
        return '<img width="32px" src="{}"/>'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

    def email(self, obj):
        return Contact.emails.filter(Speaker=obj).first()

    email.short_description = 'email'

    def phone(self, obj):
        return Contact.phone.filter(Speaker=obj).first()

    phone.short_description = 'Telefone'


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)