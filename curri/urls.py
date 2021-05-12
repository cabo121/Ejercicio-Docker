from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from .views import modificarInfo,agregarInfo,eliminarInfo,modificar,eliminar,agregar,HomePageView,CurriPageView,InfoPageView,RegistrarPageView,RegistroPageView

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('curriculum',CurriPageView.as_view(),name = 'curriculum'),
	path('info',InfoPageView.as_view(),name = 'info'),
	path('registro_success',RegistroPageView.as_view(), name = 'registro_success'),
	path('registrar/', RegistrarPageView.as_view(), name='registrar'),
	path('registrar/reset',auth_views.PasswordResetView.as_view(), name='reset'),
	path('modificar/<id>/', modificar, name = 'modificar'),
	path('eliminar/<id>/', eliminar, name = 'eliminar'),
	path('agregar/', agregar, name = 'agregar' ),
	path('modificarInfo/<id>/', modificarInfo, name = 'modificarInfo'),
	path('eliminarInfo/<id>/', eliminarInfo, name = 'eliminarInfo'),
	path('agregarInfo/', agregarInfo, name = 'agregarInfo' ),
]