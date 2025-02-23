from django import forms
from .models import Questionnaire
from .models import Anthropometry, WristDynamometry

class StudentForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = [
            'name', 'surname', 'patronymic', 'date_of_birth', 'qualification',
            'experience', 'chronic_conditions', 'mother_height', 'dad_height',
            'mother_sport', 'dad_sport'
        ]  # registration_date, photo убраны

class AnthropometryForm(forms.ModelForm):
    class Meta:
        model = Anthropometry
        fields = ['height', 'weight', 'foot_length', 'shin_length', 'thigh_length', 'arm_span',
                  'waist_circumference', 'hip_circumference', 'chest_circumference']  # registration_date не включено

class WristDynamometryForm(forms.ModelForm):
    class Meta:
        model = WristDynamometry
        fields = ['left_hand', 'right_hand']  # registration_date не включено



from .models import Account

from django import forms
from django.contrib.auth.models import User


from django import forms
from django.contrib.auth.models import User
from .models import Account



class TrainerForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)
    patronymic = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
