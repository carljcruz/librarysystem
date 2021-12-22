from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from catalogs.models import Acquisition, Book
from catalogs.forms import BookForm, AcquisitionForm
from accounts.views import home_view
from django.contrib import messages
# from django.http import HttpResponseRedirect


# Acquisition views

def create_acquisition(request):
    if request.method == "POST":
        ac_form = AcquisitionForm(request.POST)

        if ac_form.is_valid():
            ac_form.save()
            return HttpResponse("Thanks")

    else:
        ac_form = AcquisitionForm()
    context = {

        "ac_form": ac_form,
    }
    return render(request, "partials/create_acquisition.html", context=context)


# view specific book
def view_acquisition(request, title):
    acquisition = Acquisition.objects.get(title=title)

    template_name = 'view_acquisition.html'

    context = {
        'acquisition': acquisition
    }

    return render(request, template_name, context=context)


def update_acquisition(request, title):
    acquisition = Acquisition.objects.get(title=title)
    form = AcquisitionForm()
    template_name = 'view_acquisition.html'
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
            # add a message saying success
            messages.success(request, "Updated Acquisitions")
            return redirect(home_view)
        else:
            messages.warning(request, "Please see errors")
    context = {
        'acquisition': acquisition,
        'form': form,
    }
    return render(request, template_name, context=context)


def delete_acquisition(request, title_proper):
    acquisition = Acquisition.objects.get(title_proper=title_proper)
    acquisition.delete()
    messages.success(request, "Acquisition deleted")
    return redirect(home_view)

# End Acquisition views

def create_book(request):
    if request.method == "POST":
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book_form.save()
            return HttpResponse("Thanks")

    else:
        book_form = BookForm()
    context = {

        "book_form": book_form,
    }
    return render(request, "partials/create_book.html", context=context)


# view specific book
def view_book(request, title_proper):
    book = Book.objects.get(title_proper=title_proper)

    template_name = 'view_book.html'

    context = {
        'book': book
    }

    return render(request, template_name, context=context)


def update_book(request, title_proper):
    book = Book.objects.get(title_proper=title_proper)
    form = BookForm()
    template_name = 'view_book.html'
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
            # add a message saying success
            messages.success(request, "Added a new book")
            return redirect(home_view)
        else:
            messages.warning(request, "Please see errors")
    context = {
        'book': book,
        'form': form,
    }
    return render(request, template_name, context=context)


def delete_book(request, title_proper):
    book = Book.objects.get(title_proper=title_proper)
    book.delete()
    messages.success(request, "Book deleted")
    return redirect(home_view)

# TODO: DRY ( Mix everything in into one view )
