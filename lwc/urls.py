from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    #url(r'^testhome$', 'lwc.views.testhome', name='testhome'),
    url(r'^share/$', 'joins.views.share', name='share'),
    # Examples:
    #url(r'^home2/$', 'lwc.views.home2', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^about/$', 'joins.views.about', name='about'),
    url(r'^blog/$', 'joins.views.blog', name='blog'),
    url(r'^pizza/$', 'joins.views.pizza', name='pizza'),
    url(r'^burgers/$', 'joins.views.burgers', name='burgers'),
    url(r'^brisket/$', 'joins.views.brisket', name='brisket'),
    url(r'^rankpizza/$', 'joins.views.rankpizza', name='rankpizza'),

    url(r'^logout/$', 'joins.views.logout_view', name='auth_logout'),
    url(r'^login/$', 'joins.views.login_view', name='auth_login'),

    
)