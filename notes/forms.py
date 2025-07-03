from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """
    Form for creating and editing notes
    
    Uses ModelForm to automatically create form fields based on the Note model
    Adds Bootstrap classes for styling
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        } 