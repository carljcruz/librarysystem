from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from catalogs.models import Book, Acquisition

# lmao
class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # title proper model
        self.fields["title_proper"].label = ""
        self.fields["responsibility"].label = ""
        self.fields["preferred_title"].label = ""
        self.fields["parallel_title"].label = ""
        self.fields["main_creator"].label = ""
        self.fields["added_entry_creator"].label = ""
        self.fields["contributors"].label = ""
        self.fields["added_entry_corporate"].label = ""

        # publication model
        self.fields["place_of_publication"].label = ""
        self.fields["publisher"].label = ""
        self.fields["edition"].label = ""
        self.fields["extent_of_text"].label = ""
        self.fields["dimension"].label = ""
        self.fields["series"].label = ""
        self.fields["supplementary_content"].label = ""
        self.fields["content_type"].label = ""
        self.fields["media_type"].label = ""
        self.fields["carrier_type"].label = ""
        self.fields["identifier_isbn"].label = ""
        self.fields["url"].label = ""

        # TODO: access point model

        # local information model
        self.fields["call_number"].label = ""
        self.fields["accession"].label = ""
        self.fields["language"].label = ""
        self.fields["library_location"].label = ""
        self.fields["book_catalog_image"].label = ""

    class Meta:
        model = Book
        fields = "__all__"


class AcquisitionForm(ModelForm):
    class Meta:
        model = Acquisition
        fields = '__all__'