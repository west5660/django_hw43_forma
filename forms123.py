from django import forms
from colorfield.fields import ColorField

class Nashaforma(forms.Form):
    name=forms.CharField(label='Ваше имя')
    num=forms.IntegerField(label='Номер', required=False, max_value=100, initial=12,help_text='werwer')

class Nashaforma2(forms.Form):
    name = forms.CharField(label='Имя животного')
    age = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    poroda = forms.CharField(label='Порода')
    color = forms.CharField(label='Цвет', widget=forms.TextInput(attrs={'type': 'color'}))
    food = forms.CharField(label='Любимая еда')
    foto = forms.ImageField(label='Изображение животного')

