from django import forms

sample_markdown = \
"""
"""

class NewPageForm(forms.Form):
    title = forms.CharField(
        label="Page Title", 
        widget=forms.TextInput(attrs={"placeholder": "Page Title"}),
        required=True,
    )

    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"placeholder": sample_markdown}),
    )

class EditPageForm(forms.Form):
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(),
    )