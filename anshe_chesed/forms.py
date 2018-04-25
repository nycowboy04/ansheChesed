from django.forms import ModelForm

class CACForm(ModelForm):
    class Meta():
        model=CAC
        fields=('first_name','last_name','email','address1','address2','city','state','zip','poomo')
        
