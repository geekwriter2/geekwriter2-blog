from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from blogging.models import Post
from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.views import Feed
from django.urls import reverse


class BlogFeed(Feed):
    title = "geekwriter2-blog"
    link = "/latest/"
    description = "RSS feed of geekwriter2-blog"

    def items(self):
        return Post.objects.order_by('created_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return item.title


class atomFeed(Feed):
    feed_type = Atom1Feed

    """
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    """