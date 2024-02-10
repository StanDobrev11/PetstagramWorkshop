from django import forms

from petstagram.core.mixins import ReadonlyFieldMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm, ReadonlyFieldMixin):
    class Meta:
        model = Pet
        fields = ['name', 'birth_date', 'photo_address']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),  # 'Pet name' will be displayed on the field
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'photo_address': forms.URLInput(attrs={'placeholder': 'Link to image'})
        }

        labels = {
            'name': 'Pet name',
            'birth_date': 'Date of birth',
            'photo_address': 'Link to image',
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    readonly_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    class Meta(PetBaseForm.Meta):
        pass


class PetDeleteForm(PetBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()
        # self.fields['name'].widget.attrs['readonly'] = True
        # self.fields['birth_date'].widget.attrs['readonly'] = True
        # self.fields['photo_address'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
