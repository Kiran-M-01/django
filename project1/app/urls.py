from django.urls import path
from . import views 


urlpatterns = [
    path('sample/',views.sample),
    path('sum/<int:a>/<int:b>/',views.sum),
    path('isvowel/<ch>/', views.isvowel),
    # IF - IF ELSE
    path("positive/<int:num>/",views.positive),
    path("vote/<int:age>/",views.vote),
    path("name/<name>/",views.name),
    path("fruit_list/<fruit>/",views.fruits),
    path("login/",views.login),
    path("evenodd/<int:num>/",views.evenodd),
    path("adult/<int:age>/",views.adult),
    path("result/<int:marks>/",views.result),
    path("userlogin/",views.userlogin),
    path("stock/<int:quantity>",views.stock),

# ELIF AND NESTED IF
    path('char_check/<ch>/',views.char_check),

    # EL IF 5 EXAMPLES
    path("char/<str:ch>/", views.char_check),
    path("grade/<int:marks>/", views.grade),
    path("month/<int:num>/", views.month),
    path("weekday/<str:day>/", views.weekday),
    path("signal/<str:color>/", views.signal),

    # NESTED IF 5 EXAMPLES
    path("citizen/<int:age>/", views.nested1),
    path("result/<int:marks>/", views.nested2),
    path("salary/<int:salary>/", views.nested3),
    path("leep_year/<int:year>/", views.nested5),
    path("temperature/<int:temp>/", views.nested6),


    # FOR LOOP
    path('char/',views.char),
    path('products_list/',views.products),
    path('products_ui/',views.products_ui),
    path("product_details/<int:id>/", views.product_detail, name="product_detail"),


]
