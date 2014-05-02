from mysite.models import createuser, createquestion, question_type
from django.contrib import admin


admin.site.register(createuser)
admin.site.register(createquestion)
admin.site.register(question_type)