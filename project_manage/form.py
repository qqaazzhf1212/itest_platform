from django import forms
from project_manage.models import Project


# class ProjectForm(forms.Form):
#     name = forms.CharField(label="名字", max_length=100)
#     describe = forms.CharField(label="描述", widget=forms.Textarea)
#     status = forms.BooleanField(label="状态", required=False)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
        exclude = ['create_time', 'update_time']
