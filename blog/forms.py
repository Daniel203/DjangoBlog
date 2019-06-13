from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder' : 'Lascia un commento!',
            })
    )
