from django.forms import ModelForm

from traitementImage.models import TraitementImage

class TraitementImageForm(ModelForm):
    class Meta:
        model = TraitementImage 
        fields = ('image','intensite')