from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Hero, AboutSection, Experience, ContactInfo
from .serializers import (
    HeroSerializer, AboutSectionSerializer,
    ExperienceSerializer, ContactInfoSerializer
)

class HeroView(RetrieveAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get_object(self):
        return Hero.objects.first()

class AboutView(RetrieveAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

    def get_object(self):
        return AboutSection.objects.first()

class ExperienceListView(ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ContactInfoListView(ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    

from .models import Footer
from .serializers import FooterSerializer

class FooterView(RetrieveAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

    def get_object(self):
        return Footer.objects.first()