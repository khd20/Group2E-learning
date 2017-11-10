from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from courses.views import CourseListView
#from . import views
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView



urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    #url(r'^accounts/profile/$', ),
    #url(r'^accounts/profile/$', views.home(), name='home'),
    #restore password urls
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^course/', include('courses.urls')),
    url (r'^students/', include ('students.urls')),
    url(r'^$', CourseListView.as_view(), name='course_list'),

    #url(r'accounts/', include('accounts.urls')),

]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)