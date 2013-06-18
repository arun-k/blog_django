from django.conf.urls import patterns, include, url
from views import user_home,post_edit,new_post,single_post

urlpatterns = patterns('',(r'^([A-Za-z\d]+)/$',user_home),(r'^[A-Za-z\d]+/postedit/(\d+)/$',post_edit),(r'^([A-Za-z\d]+)/newpost/$',new_post),(r'^[A-Za-z\d]+/post/(\d+)$',single_post),
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
