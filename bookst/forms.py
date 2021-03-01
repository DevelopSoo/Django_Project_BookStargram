from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    _type = forms.ChoiceField(widget=forms.RadioSelect,
                              label='종류',
                              choices=Post.POST_TYPES,
                              required=True
                              )
    class Meta:
        model = Post
        fields = ['title', '_type', 'content', 'image']
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '이미지',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }