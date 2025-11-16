from django import forms
from mmorpg_app.models import Character, Player, Guild


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'level', 'class_name', 'role', 'gold', 'player', 'guild']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
        }