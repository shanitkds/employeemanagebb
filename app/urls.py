from django.urls import path,include
from .views import *

urlpatterns = [
    path('',viewemployee,name="view"),
    path('viewdetails/<int:id>/',employeedetails,name="emdetails"),
    path('addemployee/',addemployee,name="addemployee"),
    path('edit/<int:id>',editemployee,name="edit"),
    
    # API
    
    path('employee/',EmployeeAPIView.as_view()),
    path('employeedetails/<int:id>/',EmployeeDetailsApIView.as_view()),
]
