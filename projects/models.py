from django.db import models

class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    emoji       = models.CharField(max_length=10, default='🔹')
    gradient    = models.CharField(max_length=100, default='from-blue-900/60 to-[#0B1120]')
    tags        = models.JSONField(default=list)
    github      = models.URLField(blank=True)
    demo        = models.URLField(blank=True, null=True)
    order       = models.IntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title