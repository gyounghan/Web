from django import forms

class CommentForm(forms.Form):
    content = forms.CharField(
        widget = forms. TextInput(
            attrs = {
                'class' : 'content',
                'placeholder' : '댓글을 달아주세요'
            }
        )
    )