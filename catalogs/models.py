from typing import Type
from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from accounts.models import MyUser

from core.models import TimeStampedModel

# Book Models


class Book(TimeStampedModel):

    # placeholder choices 1
    CHOICE_1 = "Choice 1"
    CHOICE_2 = "Choice 2"
    CHOICE_3 = "Choice 3"
    # placeholder choices 2
    THE_CHOICES = [
        (CHOICE_1, "Choice 1"),
        (CHOICE_2, "Choice 2"),
        (CHOICE_3, "Choice 3"),
    ]

    # title proper model
    title_proper = models.CharField(max_length=255)
    responsibility = models.CharField(max_length=255)
    preferred_title = models.CharField(max_length=255)
    parallel_title = models.CharField(max_length=255)
    main_creator = models.CharField(max_length=255)
    added_entry_creator = models.CharField(max_length=255)
    contributors = models.CharField(max_length=255)
    added_entry_corporate = models.CharField(max_length=255)

    # publication model
    place_of_publication = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    # date_of_publication = models.DateField()
    edition = models.CharField(max_length=255)
    extent_of_text = models.CharField(max_length=255)
    dimension = models.CharField(max_length=10)
    series = models.CharField(max_length=10)
    supplementary_content = models.CharField(
        max_length=10, choices=THE_CHOICES, default=CHOICE_1
    )
    content_type = models.CharField(
        max_length=10, choices=THE_CHOICES, default=CHOICE_1
    )
    media_type = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_1)
    carrier_type = models.CharField(
        max_length=10, choices=THE_CHOICES, default=CHOICE_1
    )
    identifier_isbn = models.CharField(max_length=11)
    url = models.CharField(max_length=255)

    # access point model

    # local information model
    call_number = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_2)
    accession = models.CharField(max_length=255)
    language = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_1)
    library_location = models.CharField(
        max_length=10, choices=THE_CHOICES, default=CHOICE_1
    )
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name="updated_by", null=True
    )
    # TODO: electronic access
    book_catalog_image = models.CharField(
        max_length=10
    )  # TODO: replace this with an image field

    ## This can be done with django-simple-history
    # TODO: entered by
    # TODO: updated by

    def __str__(self):
        return f"Book {self.title_proper}"


class Acquisition(TimeStampedModel):

    # according to django docs, use textchoices
    class DepartmentChoices(models.TextChoices):
        LIBRARY = "LB", _("Library")
        IT_DEPT = "IT", _("IT")
        HR_DEPT = "HR", _("HR")
        TEACHING = "TC", _("Teaching")

    class ModeChoices(models.TextChoices):
        PURCHASE = "PR", _("Purchase")
        BORROW = "BR", _("Borrow")

    class LocationChoices(models.TextChoices):
        BOOKFAIR = "BF", _("Bookfair")
        SOMEWHERE = "SW", _("Somewhere")

    # Dummy persons
    # TODO: Replace this with users? OR list of real users
    class PeopleChoices(models.TextChoices):
        TAN = "TA", _("Prof Tan")
        ADVINCULA = "AD", _("Dr. Advincula")

    class TypeChoices(models.TextChoices):
        BOOK = "BO", _("Book")
        LETTER = "LT", _("Letter")

    class StatusChoices(models.TextChoices):
        ACQUIRED = "AC", _("Acquired")
        BOUGHT = "BT", _("Bought")

    class DealerChoices(models.TextChoices):
        FOREFRONT = "FF", _("Forefront")
        UPFRONT = "UF", _("Upfront")

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    year_of_pub = models.CharField(max_length=4)
    isbn = models.CharField(max_length=13)
    quantity = models.CharField(max_length=5)
    unit_price = models.CharField(max_length=10)
    discount = models.CharField(max_length=10)
    edition = models.CharField(max_length=10)
    total_price = models.CharField(max_length=10)
    net_price = models.CharField(max_length=10)
    # department choices
    department = models.CharField(
        max_length=2,
        choices=DepartmentChoices.choices,
        default=DepartmentChoices.LIBRARY,
    )
    mode = models.CharField(
        max_length=2,
        choices=ModeChoices.choices,
        default=ModeChoices.PURCHASE,
    )
    location = models.CharField(
        max_length=2,
        choices=LocationChoices.choices,
        default=LocationChoices.BOOKFAIR,
    )
    date = models.DateField(default=datetime.date.today)
    budget = models.CharField(max_length=10)
    recom_by = models.CharField(
        max_length=2, choices=PeopleChoices.choices, default=PeopleChoices.TAN
    )

    type = models.CharField(
        max_length=2, choices=TypeChoices.choices, default=TypeChoices.BOOK
    )
    status = models.CharField(
        max_length=2, choices=StatusChoices.choices, default=StatusChoices.ACQUIRED
    )
    dealer = models.CharField(
        max_length=2, choices=DealerChoices.choices, default=DealerChoices.FOREFRONT
    )
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name="acquisition_updated_by",
        null=True,
    )

    # check if it belongs to the lib  ( just a testing formality)
    def is_library(self):
        return self.department in {self.DepartmentChoices.LIBRARY}

    def __str__(self):
        return f"Title:{self.title} Publisher: {self.publisher}"


class Periodicals(models.Model):

    class PeriodicalChoices(models.TextChoices):
        CHOICE_1 = "C1", _("Choice 1")
        CHOICE_2 = "C2", _("Choice 2")
        CHOICE_3 = "C3", _("Choice 3")


    title = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    issue = models.CharField(max_length=255)

    