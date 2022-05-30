from django.forms import ModelForm, widgets
from .models import GENDERS, Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "contact_number",
            "address",
            "admit_date",
            "course",
            "year",
            "section",
        ]
        widgets = {
            "gender": widgets.RadioSelect(choices=GENDERS),
            "admit_date": widgets.DateInput(attrs={"type": "date"}),
        }
