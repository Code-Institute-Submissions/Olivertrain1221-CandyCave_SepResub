from django import forms
from .models import Sweet, Category

class SweetForm(forms.ModelForm):

    class Meta:
        model = Sweet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(e.id, e.get_friendly_name()) for e in categories]

        self.fields['category'].choiuces = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black round-0'
