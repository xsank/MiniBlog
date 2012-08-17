#-*-coding:utf-8-*-

from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    subject=forms.CharField(max_length=50,label=('主题(必填)'))
    email=forms.EmailField(label=('邮箱(必填)'))
    message=forms.CharField(widget=forms.Textarea(),label=('内容(必填)'))
    captcha=CaptchaField(label=('验证码(必填)'))

    def cleanData(self):
        message=self.cleaned_data['message']
        wordcount=len(message.split())
        if wordcount<4:
            raise forms.ValidationError(unicode('，填的内容太少了，请认真填写！'))
        if wordcount>100:
            raise forms.ValidationError(unicode('你填的也太多了吧，复制粘贴的？'))
        return message