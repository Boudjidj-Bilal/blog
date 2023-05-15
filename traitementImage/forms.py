from django.forms import ModelForm

from traitementImage.models import TraitementImage
from django import forms


class TraitementImageForm(ModelForm):
    class Meta:
        model = TraitementImage 
        fields = ('image','intensite')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'required': True}),
            # 'intensite': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'intensite': forms.NumberInput(attrs={'min': 0, 'max': 255, 'class': 'form-control-range', 'type': 'range', 'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['intensite'].widget.attrs.update({'class': 'form-control-range'})
        # self.fields['my_integer_field'].widget.attrs.update({'style': 'width: 100%'})