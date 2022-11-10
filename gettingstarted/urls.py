from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("v2", hello.views.index_v2, name="index_v2"),
    path("joinnow", hello.views.joinnow, name="joinnow"),
    path("createaccount", hello.views.createaccount, name="createaccount"),
    path("subsuccessful", hello.views.subsuccessful, name="subsuccessful"),
    path("accountinfo", hello.views.accountinfo, name="accountinfo"),
    path("assets", hello.views.assets, name="assets"),
    path("assets-2-epf", hello.views.assets_2_epf, name="assets-2-epf"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
