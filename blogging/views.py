# polling/views.py

from django.shortcuts import render
from django.http import Http404
from blogging.models import Category, Post
from django.http import HttpResponse, HttpResponseRedirect, Http404

def list_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            post.score += 1
        else:
            post.score -= 1
        post.save()

    context = {'poll': post}
    return render(request, 'polling/detail.html', context)


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")