from django import forms
from schoolApp.models import schoolApp
from schoolApp.models import Teacher1

class studentmodelform(forms.ModelForm):
    class Meta:
        model=schoolApp
        fields='__all__'

class teachermodelform(forms.ModelForm):
    class Meta:
        model=Teacher1
        fields='__all__'
