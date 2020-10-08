from profile import Profile

from django.contrib import admin

# Register Profile model
from profile_cv.models import Profile_cv,Experience,Education,Programing_Language,WorkFlow,Awards


@admin.register(Profile_cv)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','address','phone','email')
    list_filter = ['created']
    search_fields = ('first_name','last_name','address','phone','email','des')
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle','time_line','created','updated')
    list_filter = ['created']
    search_fields = ('title','subtitle','time_line')
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title','degree','GPA','time_line','created','updated')
    list_filter = ['created']
    search_fields = ('title','detail','degree','GPA')
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Programing_Language)
class ProgramingLangAdmin(admin.ModelAdmin):
    list_display = ['lang']
    list_filter = ['created']
    search_fields = ['lang']
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(WorkFlow)
class WorkFlowAdmin(admin.ModelAdmin):
    list_display = ['workflow']
    list_filter = ['created']
    search_fields = ['workflow']
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ['awards']
    list_filter = ['created']
    search_fields = ['awards']
    date_hierarchy = 'created'
    ordering = ['created']
