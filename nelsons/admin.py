from django.contrib import admin

from .models import Nelson

class NelsonAdmin(admin.ModelAdmin):    
	list_display = ('name', 'edx_user', 'created_date', 'was_active_recently')

admin.site.register(Nelson, NelsonAdmin)
