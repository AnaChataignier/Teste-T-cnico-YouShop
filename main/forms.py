from django import forms
from .models import Profile, PlantedTree, Account


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["about"]
        labels = {"about": "About me"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["about"].widget.attrs.update(
            {"class": "form-control", "rows": "5"}
        )  # Adiciona classes CSS e ajusta o tamanho do campo


class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ['age', 'tree', 'account', 'location']
        widgets = {
            'tree': forms.Select(attrs={'class': 'form-control'}),
            'account': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(PlantedTreeForm, self).__init__(*args, **kwargs)
        self.fields["account"].queryset = Account.objects.filter(members=user)

    def save(self, commit=True):
        instance = super(PlantedTreeForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
