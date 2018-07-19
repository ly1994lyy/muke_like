import re
from django import forms

from operation.models import UserAsk


class UserAskForm(forms.Form):
    class Meta:
        model = UserAsk
        fileds = ['name', 'mobile', 'course_name']

    def clean_moblie(self):
        moblie = self.cleaned_data['moblie']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(moblie):
            return moblie
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")