from django import forms
from django.forms.models import ModelForm
from activity.models import *

class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        fields = ('name','description',)

class upload_artifact(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    content = forms.FileField()
    activity = forms.CharField(max_length=30)
    technique = forms.CharField(max_length=30)
    
    def get_fields(self):
        return self.cleaned_data
        
class ActivityCreateForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'description', 'progress', 'date_start','date_end','project','users','activities_required','activities_super','activities_successor','roles','software_process','techniques')

