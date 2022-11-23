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
    path("assets-3-insurance", hello.views.assets_3_insurance, name="assets-3-insurance"),
    path("assets-4-investment", hello.views.assets_4_investment, name="assets-4-investment"),
    path("assets-5-property", hello.views.assets_5_property, name="assets-5-property"),
    path("assets-6-vehicles", hello.views.assets_6_vehicles, name="assets-6-vehicles"),
    path("assets-7-others", hello.views.assets_7_others, name="assets-7-others"),
    path("index-v3", hello.views.index_v3, name="index-v3"),
    path("edits-assets-bank", hello.views.edits_assets_bank, name="edits-assets-bank"),
    path("edits-assets-epf", hello.views.edits_assets_epf, name="edits-assets-epf"),
    path("edits-assets-insurance", hello.views.edits_assets_insurance, name="edits-assets-insurance"),
    path("edits-assets-investment", hello.views.edits_assets_investment, name="edits-assets-investment"),
    path("edits-assets-property", hello.views.edits_assets_property, name="edits-assets-property"),
    path("edits-assets-vehicles", hello.views.edits_assets_vehicles, name="edits-assets-vehicles"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
