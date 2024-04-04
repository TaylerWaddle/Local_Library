from django.urls import path
from .views import index, BookListView, BookDetailView, AuthorListView, AuthorDetailView, LoanedBooksByUserListView, LoanedBooksLibrarianListView, renew_book_librarian, AuthorCreate, AuthorDelete, AuthorUpdate, BookCreate, BookUpdate, BookDelete
urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-books'),
    path('loanedbooks/', LoanedBooksLibrarianListView.as_view(), name='loaned-books'),
    path('book/<uuid:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
    path('book/create/', BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]