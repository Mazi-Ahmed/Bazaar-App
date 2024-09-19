from django import forms
from .models import DialogueText

class DialogueTextStart(forms.ModelForm):
    class Meta:
        model = DialogueText
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }