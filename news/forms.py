# -*- coding: utf-8 -*-
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from news.models import News


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = News
        fields = '__all__'
