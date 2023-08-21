from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class signupform(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email address'}))
    first_name = forms.CharField(label="",max_length=100 ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        
    def __init__(self, *args,**kwargs):
        super(signupform, self).__init__(self, *args,**kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].label =''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>required. 150 character or fewer letters, digits and @/./+/-/_ only</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted" small><li>your password can\'t be too similar to your other personal information.</li><li>your password must contain at least 8 characters</li><li>your passwprd can\'t be commonly used password.</li><li>your password can\'t be entirely numerical</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm your password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>enter the same password as before for verification.</small></span>'
        
        