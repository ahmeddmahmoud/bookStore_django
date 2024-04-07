from django.shortcuts import render, get_object_or_404,redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

## imports from your created files
from books.models import book
from books.forms import  BookModelForm

books = [
    {"id": 1, "title": "book1", "no_pages": 150, "author": "author1", "price": 150, "image": "1.png"},
    {"id": 2, "title": "book2", "no_pages": 150, "author": "author2", "price": 150, "image": "2.png"},
    {"id": 3, "title": "book3", "no_pages": 150, "author": "author3", "price": 150, "image": "3.png"},
    {"id": 4, "title": "book4", "no_pages": 150, "author": "author4", "price": 150, "image": "4.png"},
    {"id": 5, "title": "book5", "no_pages": 150, "author": "author5", "price": 150, "image": "5.png"},
    {"id": 6, "title": "book6", "no_pages": 150, "author": "author6", "price": 150, "image": "6.png"},
    {"id": 7, "title": "book7", "no_pages": 150, "author": "author7", "price": 150, "image": "7.png"},
    {"id": 8, "title": "book8", "no_pages": 150, "author": "author8", "price": 150, "image": "8.png"},
    {"id": 9, "title": "book9", "no_pages": 150, "author": "author9", "price": 150, "image": "9.png"},
]

def book_details(request, id):
    filtered_books = filter(lambda book: book['id'] == id, books)
    filtered_books = list(filtered_books)
    if filtered_books:
        book = filtered_books[0]
        return render(request, "books/details.html", context={"book":book})

def books_home(request):
    return render(request, "books/home.html", context={"books": books}, status=200)

def contact_us(request):
    return render(request, "books/contactus.html", status=200)

def about_us(request):
    return render(request, "books/aboutus.html", status=200)

def books_index(request):
    books  = book.objects.all()
    return render(request, "books/homedatabase.html",
                  context={"books": books})

@login_required
def book_show(request, id):
    bookdata = get_object_or_404(book, pk=id)
    return render(request, "books/detailsdatabase.html", context={"bookdata": bookdata})

@login_required
def book_delete(request, id):
    bookdata = get_object_or_404(book, pk=id)
    bookdata.delete()
    url = reverse("homedatabase")
    return redirect(url)

def book_create(request):
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        newbook = book(title=request.POST["title"], price=request.POST["price"], author=request.POST["author"],
                          no_pages=request.POST["no_pages"], image=image)
        newbook.save()
        url = reverse("homedatabase")
        return redirect(url)
    return  render(request, 'books/create.html')

def book_update(request,id):
    bookdata = get_object_or_404(book, pk=id)
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = bookdata.image
        bookdata.title = request.POST["title"]
        bookdata.author = request.POST["author"]
        bookdata.price = request.POST["price"]
        bookdata.no_pages = request.POST["no_pages"]
        bookdata.image = image
        bookdata.save()
        url = reverse("homedatabase")
        return redirect(url)

    return render(request, "books/update.html", {"bookdata":bookdata})

@login_required
def book_create_forms(request):
    form = BookModelForm()
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        form = BookModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            url = reverse("homedatabase")
            return redirect(url)

    return render(request, 'books/forms/create.html', context={'form':form})

@login_required
def book_edit_forms(request, id):
    bookdata= get_object_or_404(book, pk=id)
    form = BookModelForm(instance=bookdata)
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES, instance=bookdata)
        if form.is_valid():
            form.save()
            url = reverse("homedatabase")
            return redirect(url)

    return render(request, 'books/forms/update.html',
              context={"form": form})


