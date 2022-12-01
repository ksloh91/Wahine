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
    path("contactus", hello.views.contactus, name="contactus"),
    path("createaccount", hello.views.createaccount, name="createaccount"),
    path("createaccount-1", hello.views.createaccount_1, name="createaccount-1"),
    path("createaccount-2", hello.views.createaccount_2, name="createaccount-2"),
    path("createaccount-3", hello.views.createaccount_3, name="createaccount-3"),
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
    path("edits-assets-others", hello.views.edits_assets_others, name="edits-assets-others"),
    path("liabilities-1-creditcard", hello.views.liabilities_1_creditcard, name="liabilities-1-creditcard"),
    path("liabilities-2-personalloan", hello.views.liabilities_2_personalloan, name="liabilities-2-personalloan"),
    path("liabilities-3-vehiclesloan", hello.views.liabilities_3_vehiclesloan, name="liabilities-3-vehiclesloan"),
    path("liabilities-4-property", hello.views.liabilities_4_property, name="liabilities-4-property"),
    path("liabilities-5-others", hello.views.liabilities_5_others, name="liabilities-5-others"),
    path("edits-liabilities-creditcard", hello.views.edits_liabilities_creditcard, name="edits-liabilities-creditcard"),
    path("edits-liabilities-personalloan", hello.views.edits_liabilities_personalloan, name="edits-liabilities-personalloan"),
    path("edits-liabilities-vehiclesloan", hello.views.edits_liabilities_vehiclesloan, name="edits-liabilities-vehiclesloan"),
    path("edits-liabilities-property", hello.views.edits_liabilities_property, name="edits-liabilities-property"),
    path("edits-liabilities-others", hello.views.edits_liabilities_others, name="edits-liabilities-others"),
    path("overview-assets", hello.views.overview_assets, name="overview-assets"),
    path("overview-liabilities", hello.views.overview_liabilities, name="overview-liabilities"),
    path("header-loggedin", hello.views.header_loggedin, name="header-loggedin"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
