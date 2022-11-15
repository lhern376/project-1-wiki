from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
import random
import markdown2
from encyclopedia.forms import NewPageForm, EditPageForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    entry_content = util.get_entry(title)
    if entry_content:
        context = {
            "title": title,
            "entry_content": markdown2.markdown(
                entry_content, extras=[
                    "fenced-code-blocks", 
                    "code-friendly",
                    "tables",
                    "wiki-tables",
                    "numbering",
                    "footnotes",
                    "header-ids",
                    "task_list",
                ]
            ),
        }
        return render(request, "encyclopedia/page_entry.html", context)
    else:
        return render(request, "encyclopedia/page_error.html", {"title": title,})
    

def search(request):
    title = request.GET["q"].strip()
    entry_content = util.get_entry(title)
    if entry_content:
        title = title.lower().title()
        return HttpResponseRedirect(reverse("entry-page", args=(title,))) 
    else: 
        title_lowercase = title.lower()
        entries_all = util.list_entries()
        entries_contain = list(entry for entry in entries_all if title_lowercase in entry.lower())

        context = {
            "query": title,
            "entries": entries_contain,
        }
        return render(request, "encyclopedia/page_results.html", context)


def new_page(request):
    error_message = None
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if not util.get_entry(title):
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry-page", args=(title,))) 

            error_message = title

    else:
        # form = NewPageForm(initial={"content": sample_markdown})
        form = NewPageForm(initial={"content": "# (Page Title)\n ***"})

    context = {
        "error": error_message,
        "form": form,
    }
    return render(request, "encyclopedia/page_new.html", context)


def edit_page(request, title):
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry-page", args=(title,)))             

    else:
        form = EditPageForm(initial={"content": util.get_entry(title)})

    context = {
        "title": title,
        "form": form,
    }
    return render(request, "encyclopedia/page_edit.html", context)


def random_page(request):
    entries_all = util.list_entries()
    title = random.choice(entries_all)
    return HttpResponseRedirect(reverse("entry-page", args=(title,)))             


