from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

from .models import Book, Author, BookInstance, Genre


def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )


from django.views import generic

#class BookListView(generic.ListView):
#    model = Book


class BookListView(generic.ListView):
    model = Book

    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book



class AuthorListView(generic.ListView):
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

    def Author_detail_view(request,pk):
        try:
            author_id=Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404("Author does not exist")

        #book_id=get_object_or_404(Book, pk=pk)
    
        return render(
            request,
            'catalog/author_detail.html',
            context={'author':author_id,}
        )

