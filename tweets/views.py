from django.views.generic import DetailView, ListView

from tweets.models import Tweet


class TweetDetailView(DetailView):
    template_name = 'tweets/tweet_detail_view.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Tweet.objects.get(pk=pk)


class TweetListView(ListView):
    template_name = 'tweets/tweet_list_view.html'
    queryset = Tweet.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        context['tweets_list'] = Tweet.objects.all()
        return context
