from django import forms
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from .models import Article
from ckeditor.fields import RichTextFormField



class NewArticleForm(forms.ModelForm):
    titulo = forms.CharField(max_length=255)
    subtitulo = forms.CharField(max_length=255)
    contenido = forms.CharField(widget=CKEditorWidget())  # Utiliza CKEditorWidget para el campo contenido
    autor = forms.ModelChoiceField(queryset=User.objects.all())
    fecha_creacion = forms.DateField(widget=forms.DateInput(attrs={'readonly': 'readonly'}))
    imagen = forms.ImageField()
    
    class Meta:
        model = Article
        fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_creacion', 'imagen']
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form_control', 'placeholder':'Título'}),
            'subtitulo': forms.TextInput(attrs={'class':'form_control', 'placeholder':'Subtítulo'}),
            'contenido': RichTextFormField(config_name="default", attrs={'placeholder':'Contenido'}),
            'autor': forms.TextInput(attrs={'class':'form_control', 'placeholder':'Autor'}),
            'fecha_creacion': forms.TextInput(attrs={'class':'form_control', 'placeholder':'Fecha'}),
            'imagen': forms.TextInput(attrs={'class':'form_control', 'placeholder':'Imagen'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_creacion'].widget.attrs['readonly'] = True