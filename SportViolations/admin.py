from django.contrib import admin
from .models import Profile, Questionnaire, Anthropometry, WristDynamometry, Account

admin.site.register(Profile)

admin.site.register(Questionnaire)

admin.site.register(Anthropometry)

admin.site.register(WristDynamometry)

admin.site.register(Account)

