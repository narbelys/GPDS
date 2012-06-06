from django import forms

class upload_artifact(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    content = forms.FileField()
    activity = forms.CharField(max_length=30)
    technique = forms.CharField(max_length=30)
    
    def get_fields(self):
        return self.cleaned_data