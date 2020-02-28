from django.shortcuts import render
from bookmark.models import Bookmark
# Create your views here.


class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark