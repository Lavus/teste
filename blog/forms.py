from django.forms import ModelForm, Form, CharField, FileField, ImageField
from multiupload.fields import MultiImageField
from .models import Imagem, Depoimento, Destaque

class NameForm(Form):
    your_name = CharField(label='Your name', max_length=100)

class ImageUploadForm(Form):
    """Image upload form."""
    image = ImageField()

class UploadFileForm(Form):
    title = CharField(max_length=50)
    file = FileField()

class ImagemForm(ModelForm):
    imagem = MultiImageField(label='Select a file', min_num=1, max_num=2, max_file_size=(1024*1024*10))
    class Meta:
        model = Imagem
        fields = ["album","titulo"]

class DepoimentoForm(ModelForm):
    imagem = MultiImageField(label='Select a file', min_num=1, max_num=2, max_file_size=(1024*1024*10))
    class Meta:
        model = Depoimento
        fields = ["autor","titulo","descricao"]

class DestaqueForm(ModelForm):
    imagem = MultiImageField(label='Select a file', min_num=1, max_num=2, max_file_size=(1024*1024*10))
    class Meta:
        model = Destaque
        fields = ["autor","titulo","descricao"]
