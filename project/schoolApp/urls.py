from django.urls import path

from schoolApp.views import admis
from schoolApp.views import admis_report
from schoolApp.views import Teacher
from schoolApp.views import Teacher_report
from schoolApp.views import deletestudent
from schoolApp.views import deleteteacher

from schoolApp.views import updatestudent

from schoolApp.views import updateteacher


urlpatterns = [

    path('admis/',admis),
    path('admisre/',admis_report),
    path('teacher/',Teacher),
    path('teacherre/',Teacher_report),
    path('delete/<int:id>',deletestudent),
    path('delete/<int:id>',deleteteacher),
    
    path('update/<int:id>',updatestudent),

    path('update1/<int:id>',updateteacher),


]