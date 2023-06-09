from django import forms
from BlogApp.models import Comment
class CommentForm(forms.ModelForm):
	class Meta:
 		model=Comment
 		fields=('name','email','body')

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)