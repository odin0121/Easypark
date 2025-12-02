from django.urls import path
import adminapp.views

urlpatterns = [
    path('', adminapp.views.index, name='index'),
    path('ad_home/', adminapp.views.ad_home, name="ad_home"),
    path('addbuilding/', adminapp.views.addbuilding, name="addbuilding"),
    # path('addpar_dtls/', adminapp.views.addpar_dtls, name="addpar_dtls"),
    path('admin_log/', adminapp.views.admin_log, name="admin_log"),
    path('addcmpn/', adminapp.views.addcmpn, name="addcmpn"),
    path('addvtype/', adminapp.views.addvtype, name="addvtype"),
    path('addvrate/', adminapp.views.addvrate, name="addvrate"),
    #
    # path("get_companies/", adminapp.views.get_companies, name="get_companies"),
    # path("addpar_dtls/", adminapp.views.addpar_dtls, name="addpar_dtls"),
    # path("get_building_details/", adminapp.views.get_building_details, name="get_building_details"),
    path("addpar_dtls/", adminapp.views.addpar_dtls, name="addpar_dtls"),

    path('get_building_details/', adminapp.views.get_building_details, name='get_building_details'),
    path('get_vehicle_types/', adminapp.views.get_vehicle_types, name='get_vehicle_types'),
    path('get_vehicle_rate/', adminapp.views.get_vehicle_rate, name='get_vehicle_rate'),
    path('view_all_bookings/', adminapp.views.view_all_bookings, name="view_all_bookings"),
    path('viewuser/', adminapp.views.viewuser, name="viewuser"),

    # path('admin_lod/', adminapp.views.admin_lod, name="admin_lod"),
    # path('admin_lod/', adminapp.views.admin_lod, name="admin_lod"),
    # path('admin_lod/', adminapp.views.admin_lod, name="admin_lod"),
    # path('admin_lod/', adminapp.views.admin_lod, name="admin_lod"),

]