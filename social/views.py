from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect

import os, csv

def index_view(request):
    return render(request,"social/index.html")

def book_view(request, book):
    # with open(os.path.join(settings.BASE_DIR, 'shalom/static', 'kjv.tsv')) as fd:
    #     rd = list(csv.reader(fd, delimiter='\t'))
    #     book_cc, book_up = [list(bk) for bk in rd if book == int(bk[2])], []
    #     for it in book_cc:
    #         if it[3] not in book_up:
    #             book_up.append(it[3])
    #     if len(book_up) != 0:
    #         return render(request, "social/book.html",{
    #         "book": book_up,
    #         "book_name": book_cc[0][0],
    #         "book_id": book,
    #     })
    return HttpResponseRedirect(f'/{book}/1')

def chapter_view(request, book, chapter):
    with open(os.path.join(settings.BASE_DIR, 'shalom/static', 'kjv.tsv')) as fd:
        rd = list(csv.reader(fd, delimiter='\t'))
        books = [list(bk) for bk in rd if book == int(bk[2])]
        book_cc = [list(bk) for bk in rd if book == int(bk[2]) and chapter == int(bk[3])]
        book_ids = []
        for it in books:
            if int(it[3]) not in book_ids:
                book_ids.append(int(it[3]))
        if len(book_cc) != 0:
            return render(request, "social/chapter.html",{
            "book_id": book,
            "chapter_id": chapter,
            "book_name": books[0][0],
            "book_ids": book_ids,
            "book": book_cc,
        })
    return HttpResponseRedirect('/')