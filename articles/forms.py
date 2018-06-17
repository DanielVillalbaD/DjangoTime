from django.core.exceptions import ValidationError
from django.forms import ModelForm

from articles.models import Article


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['status', 'love', 'blog']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image is not None and 'image' not in image.content_type:
            raise ValidationError('El archivo no es una imagen válida')
        return image

    def clean(self):
        super().clean()  # al llamar al método clean de la superclase garantizamos la validacion de los campos del modelo
