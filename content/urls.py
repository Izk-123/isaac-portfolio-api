from django.urls import path
from .views import FooterView, HeroView, AboutView, ExperienceListView, ContactInfoListView

urlpatterns = [
    path('hero/', HeroView.as_view(), name='hero'),
    path('about/', AboutView.as_view(), name='about'),
    path('experiences/', ExperienceListView.as_view(), name='experiences'),
    path('contact/', ContactInfoListView.as_view(), name='contact'),
    path('footer/', FooterView.as_view(), name='footer'),
]