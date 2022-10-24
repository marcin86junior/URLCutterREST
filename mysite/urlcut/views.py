from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.generics import CreateAPIView, ListAPIView
from django.views import View
from django.conf import settings

from datetime import datetime, timedelta

from .models import Link
from .serializer import LinkSerializer, LinkPremiumSerializer, EditLinkSerializer


def Homepage(request):
    """
    This view should return main page.
    """
    return render(request, 'urlcut/main.html')

class ShortenerCreateApiView(CreateAPIView):
    """
    This view should return link-generartor page.
    """
    queryset = Link.objects.all()
    serializer_class=LinkSerializer
    http_method_names = ['post']

class ShortenerCreatePremiumApiView(CreateAPIView):
    """
    This view should return link-generartor page.
    """
    queryset = Link.objects.all()
    serializer_class=LinkPremiumSerializer
    http_method_names = ['post']

class ShortenerListAPIView(ListAPIView):
    """
    This view should return list of all links.
    """
    queryset=Link.objects.all()
    serializer_class=EditLinkSerializer

class Redirector(View):
    """
    This view should redirect from "shortened link" to orginal link page and add count+1.
    """

    def get(self, request, shortener_link, *args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
        try:
            Link.objects.filter(shortened_link=shortener_link).first().increase_short_id_counter()
            redirect_link=Link.objects.filter(shortened_link=shortener_link).first().original_link
        except:
            redirect_link=Link.objects.filter(shortened_link=shortener_link).first()
            return redirect('http://127.0.0.1:8000/')
        return redirect(redirect_link)

def RemoveUnusedLinksZeroCount(request):
    links = Link.objects.filter(count=0)
    links.delete()
    return HttpResponse('Removed all links that was never was used in all time... <button onclick="history.back()">Go Back</button>')

def RemoveUnusedLinksInMinute(request):
    links = Link.objects.filter(created_at__range=["2020-01-01", datetime.now()-timedelta(minutes=1)]).filter(count=0)
    links.delete()
    return HttpResponse('Removed links never used - 1 min from "create time"... <button onclick="history.back()">Go Back</button>')

def RemoveUnusedLinksDayly(request):
    links = Link.objects.filter(created_at__range=["2020-01-01", datetime.now()-timedelta(hours=24)]).filter(count=0)
    links.delete()
    return HttpResponse('Removed links never used - 1 day from "create time"... <button onclick="history.back()">Go Back</button>')
def RemoveUsedLinksInMinute(request):
    links = Link.objects.filter(last_time_used__range=["2020-01-01", datetime.now()-timedelta(minutes=5)])
    links.delete()
    return HttpResponse('Removed used links - 5 minutes from "last time used"... <button onclick="history.back()">Go Back</button>')

def RemoveUsedLinksDayly(request):
    links = Link.objects.filter(last_time_used__range=["2020-01-01", datetime.now()-timedelta(days=5)])
    links.delete()
    return HttpResponse('Removed used links - 5 day from "last time used"... <button onclick="history.back()">Go Back</button>')

def RemoveAll(request):
    links = Link.objects.all()
    links.delete()
    return HttpResponse('Removed all data! <button onclick="history.back()">Go Back</button>')
