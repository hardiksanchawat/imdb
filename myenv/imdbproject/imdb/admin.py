from django.contrib import admin
from .models import Movieinfo

# Register your models here.
class MovieinfoAdmin(admin.ModelAdmin):
	class Meta:
		model = Movieinfo
admin.site.register(Movieinfo, MovieinfoAdmin)

