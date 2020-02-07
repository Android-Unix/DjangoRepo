from django import forms


class Create_Form(forms.Form) :
    name = forms.CharField(label = 'name :' , max_length = 200)


class Send_Mail(forms.Form) :
    subject = forms.CharField(label = 'Subject : ' , max_length = 300)
    message = forms.CharField(label = 'Message : ' , max_length = 300)
