from django.conf.urls import patterns, url
#from django.conf import settings
#from django.views.generic import TemplateView
#import django.views.static
#from views import JSONView


from pug.miner.views import connections, home, StaticView

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^(?:chart/)?(?:[Cc]onnect(?:ion)?s?|[Gg]raph)/(?P<edges>[^/]*)', connections),
    url(r'^$', 'pug.miner.views.home', name='home'),
    url(r'^explore/$', 'pug.miner.views.explore', name='explore'),
    #url(r'^static/(?P<path>.*)$', django.views.static.serve, { 'document_root': settings.STATIC_ROOT} ),
    #url(r'^media/(?P<path>.*)$', django.views.static.serve, { 'document_root': settings.MEDIA_ROOT} ),
    #url(r'^static/(?P<page>.*)\.json$', JSONView.as_view()),
    url(r'^(?P<page>.+)\.html$', StaticView.as_view()),
)
