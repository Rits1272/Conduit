from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name='authentication'
urlpatterns = [
		path('user', UserRetrieveUpdateAPIView.as_view()),
		path('users/', RegistrationAPIView.as_view()),
		path('user/login/', LoginAPIView.as_view()),
		path('api/', include('conduit.apps.profiles.urls', namespace='profiles')),
	]