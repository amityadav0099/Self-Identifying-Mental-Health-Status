from django import forms
from .models import Question
class AssessmentForm(forms.Form):

    question1 = forms.ChoiceField(
        label="How often do you feel stressed?",
        choices=[
            ('never', 'Never'),
            ('sometimes', 'Sometimes'),
            ('often', 'Often'),
            ('always', 'Always'),
        ],
        widget=forms.RadioSelect
    )

    question2 = forms.ChoiceField(
        label="How would you rate your sleep quality?",
        choices=[
            ('excellent', 'Excellent'),
            ('good', 'Good'),
            ('fair', 'Fair'),
            ('poor', 'Poor'),
        ],
        widget=forms.RadioSelect
    )
