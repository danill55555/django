from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('student_form/', views.student_form, name='student_form'),
    path('assessment/<int:student_id>/', views.assessment_view, name='assessment'),
    path('result/', views.result_view, name='result'),
    path('personal_account/<int:student_id>/', views.personal_account, name='personal_account'),
    path('export/', views.export_to_excel, name='export_to_excel'),
    path('create_trainer/', views.create_trainer, name='create_trainer'),
    path('trainers/', views.trainer_list, name='trainer_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)