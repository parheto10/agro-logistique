from django.contrib import admin
from .models import Chauffeur, Vehicule, Moto, Course, Detail_Course, Mission, detail_mission, Escale

class DetailCourseAdmin(admin.TabularInline):
   model = Detail_Course
   extra = 0

class DetailMissionAdmin(admin.TabularInline):
   model = detail_mission
   extra = 0

class EscaleAdmin(admin.TabularInline):
   model = Escale
   extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [DetailCourseAdmin]

class MissionAdmin(admin.ModelAdmin):
    inlines = [DetailMissionAdmin, EscaleAdmin]

admin.site.register(Chauffeur)
admin.site.register(Vehicule)
admin.site.register(Moto)
admin.site.register(Course, CourseAdmin)
# admin.site.register(Detail_Course)
admin.site.register(Mission, MissionAdmin)
# admin.site.register(detail_mission)
# admin.site.register(Escale)

# Register your models here.
