from rest_framework import serializers
from .models import (
    Hero, TypedRole, AboutSection, AboutParagraph, Stat,
    Experience, ExperienceTag, ContactInfo
)

class TypedRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypedRole
        fields = ['role']

class HeroSerializer(serializers.ModelSerializer):
    typed_roles = TypedRoleSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = '__all__'

class AboutParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutParagraph
        fields = ['text']

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['number', 'label']

class AboutSectionSerializer(serializers.ModelSerializer):
    paragraphs = AboutParagraphSerializer(many=True, read_only=True)
    stats = StatSerializer(many=True, read_only=True)

    class Meta:
        model = AboutSection
        fields = '__all__'

class ExperienceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceTag
        fields = ['tag']

class ExperienceSerializer(serializers.ModelSerializer):
    tags = ExperienceTagSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'