from django.urls import path, include
from . import views

urlpatterns = [
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('technician-dashboard', views.technician_dashboard_view,name='technician-dashboard'),
    #Customer urls
    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('',views.home_view,name=''),
    #chat
    path('send/<str:email>/', views.send_message, name='send_message'),
    path('conversation/<str:email>/', views.view_conversation, name='conversation'),
    path('delete/<int:message_id>', views.delete_message, name='delete_message'),

    #inquiry section
    path('aboutus', views.aboutus_view)
]


