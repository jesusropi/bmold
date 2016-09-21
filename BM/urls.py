# -*- coding: UTF-8 -*-

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.conf.urls import patterns, include, url
from BM_SOAP.views import actualizar_estadistica, ad_estadisticas_form, ad_objetos_form, actualizar_objetos
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BM.views.home', name='home'),
    # url(r'^BM/', include('BM.foo.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^seasons/?temporada=(<pk>\d+)$',get_categorias, name='categorias'),
    url(r'^BM/', include('BM.urls', namespace="BM")),
    url(r'^GC/', include('GC.urls', namespace="GC")),
    url(r'^administracion/estaditica$', ad_estadisticas_form.as_view(), name='administrar_e'),
    url(r'^administracion/objetos/$', ad_objetos_form.as_view(), name="administrar_o"), 
    url(r'^administracion/estaditica/estat/$', actualizar_estadistica, name="ac_estat"), 
    url(r'^administracion/objetos/obje/$', actualizar_objetos, name="ac_obje"), 
    
    
)
urlpatterns += staticfiles_urlpatterns()
