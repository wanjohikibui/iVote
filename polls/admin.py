from django.contrib import admin
from polls.models import Poll, Choice

class PollAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question', 'pub_date', 'was_published_today')
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)


# Register your models here.
