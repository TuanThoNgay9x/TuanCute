from django.forms import ModelForm
from .models import Post


class PortForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
