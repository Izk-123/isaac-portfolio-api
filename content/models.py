from django.db import models

class Hero(models.Model):
    # Singleton: ensure only one Hero instance exists
    greeting = models.CharField(max_length=50, default="👋 Hello, I'm")
    name_line1 = models.CharField(max_length=100, default="Isaac Michael")
    name_line2 = models.CharField(max_length=100, default="Ndoka")
    highlight_text = models.CharField(max_length=50, default="Ndoka")
    description = models.TextField(default="I build modern software systems...")
    primary_cta = models.CharField(max_length=50, default="View Projects")
    primary_cta_link = models.CharField(max_length=200, default="#projects")
    secondary_cta = models.CharField(max_length=50, default="Contact Me")
    secondary_cta_link = models.CharField(max_length=200, default="#contact")

    class Meta:
        verbose_name_plural = "Hero"
        constraints = [
            models.CheckConstraint(check=models.Q(id=1), name="single_hero_row")
        ]

    def save(self, *args, **kwargs):
        if not self.pk and Hero.objects.exists():
            raise ValueError("Only one Hero instance allowed")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Hero Section"

class TypedRole(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='typed_roles')
    role = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ['hero', 'role']

    def __str__(self):
        return self.role

class AboutSection(models.Model):
    tagline = models.CharField(max_length=100, default="About me")
    title_line1 = models.CharField(max_length=100, default="Engineer. Developer.")
    title_line2 = models.CharField(max_length=100, default="Problem Solver.")
    highlight_text = models.CharField(max_length=50, default="Problem Solver.")
    profile_emoji = models.CharField(max_length=10, default="👨‍💻")
    availability_badge = models.CharField(max_length=50, default="Available for hire")

    class Meta:
        verbose_name_plural = "About Section"
        constraints = [
            models.CheckConstraint(check=models.Q(id=1), name="single_about_row")
        ]

    def save(self, *args, **kwargs):
        if not self.pk and AboutSection.objects.exists():
            raise ValueError("Only one AboutSection instance allowed")
        super().save(*args, **kwargs)

    def __str__(self):
        return "About Section"

class AboutParagraph(models.Model):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='paragraphs')
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ['about_section', 'text']

    def __str__(self):
        return self.text[:50]

class Stat(models.Model):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='stats')
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ['about_section', 'label']

    def __str__(self):
        return f"{self.number} {self.label}"

class Experience(models.Model):
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=10, default="💼")
    color = models.CharField(max_length=7, default="#2563EB")
    bg_color = models.CharField(max_length=20, default="rgba(37,99,235,0.1)")
    text_color = models.CharField(max_length=7, default="#93C5FD")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ['role', 'organization']

    def __str__(self):
        return self.role

class ExperienceTag(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=50)

    class Meta:
        unique_together = ['experience', 'tag']

    def __str__(self):
        return self.tag

class ContactInfo(models.Model):
    icon = models.CharField(max_length=10)
    label = models.CharField(max_length=50)
    value = models.CharField(max_length=200)
    href = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Contact info"
        unique_together = ['label', 'value']

    def __str__(self):
        return self.label
    
class Footer(models.Model):
    copyright_text = models.CharField(max_length=200, default="© 2026 Isaac Michael Ndoka")
    built_with_text = models.CharField(max_length=200, default="Built with Next.js · Tailwind CSS · Framer Motion")

    class Meta:
        verbose_name_plural = "Footer"
        constraints = [
            models.CheckConstraint(check=models.Q(id=1), name="single_footer_row")
        ]

    def save(self, *args, **kwargs):
        if not self.pk and Footer.objects.exists():
            raise ValueError("Only one Footer instance allowed")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Footer Section"

class FooterLink(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name='links')
    label = models.CharField(max_length=50)
    href = models.URLField(max_length=200)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ['footer', 'label']

    def __str__(self):
        return self.label