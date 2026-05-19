from rest_framework import serializers
from .models import SkillCategory, Skill

class SkillCategorySerializer(serializers.ModelSerializer):
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = SkillCategory
        fields = ['id', 'icon', 'category', 'color', 'skills']