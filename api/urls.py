from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings
from. import endpoint

urlpatterns = [
    path('technicians/', endpoint.technician_list),
    path('customers/', endpoint.customer_list),
    path('customers-details/<int:pk>/',endpoint.customer_detail),
    path('appointments/', endpoint.appointment_list),
    path('appointments-details/<int:pk>/', endpoint.appointment_details),
    path('ddl/', endpoint.devicedischarge_list),
    path('ddl-details/<int:pk>/', endpoint.devicedischarge_details),

    
]



if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)

