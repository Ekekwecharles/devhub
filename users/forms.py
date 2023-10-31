from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs): 
        # This is a call to the super() function, which returns a temporary object of the superclass (parent class) of the ProjectForm class.
        # In other words, it's a way to call methods of the parent class.
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Desc'})

        # To clarify, the fields attribute is not a dictionary, but a list of field names you want to include in your form.
        # The self.fields refers to the dictionary-like object of form fields that Django automatically creates when you define fields in your form class.


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs): 
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']


    def __init__(self, *args, **kwargs): 
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']


    def __init__(self, *args, **kwargs): 
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})