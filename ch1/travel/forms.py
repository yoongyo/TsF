from .models import Post
from django import forms



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'Tourtype',
            'Country',
            'City',
            'Language',
            'DetailContent',
            'BriefContent',
            'HashTag',
            'MeetingPoint',
            'MeetingTime',
            'Map',
            'Direction',
            'CourseName',
            'Duration',
            'Price',
            'Minimum',
            'Maximum',
            'Price_include',
            'NotDate',
            'GuestInfo',
        ]

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
