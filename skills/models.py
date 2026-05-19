from django.db import models

class SkillCategory(models.Model):
    icon     = models.CharField(max_length=10, default='💻')
    category = models.CharField(max_length=100)
    color    = models.CharField(max_length=7, default='#2563EB')
    order    = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Skill categories'

    def __str__(self):
        return self.category


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='skills'
    )
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name