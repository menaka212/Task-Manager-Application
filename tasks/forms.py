from django import forms

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:

        model = Task

        fields = [
            'title',
            'description',
            'priority',
            'stage'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'stage': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }