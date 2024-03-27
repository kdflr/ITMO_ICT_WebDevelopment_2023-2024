from project_first_app.models import User
from django import forms


class OwnerForm(forms.ModelForm):
  class Meta:
    model = User

    fields = [
      "last_name",
      "first_name",
      "birth_date",
      "passport",
      "address",
      "nationality",
    ]