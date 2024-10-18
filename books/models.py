from django.db import models
from django.conf import settings

class Book(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('used', 'Used'),
        ('worn', 'Worn'),
    ]

    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books',
        help_text='The user who is selling the book.'
    )
    title = models.CharField(max_length=255, help_text='Title of the book.')
    author = models.CharField(max_length=255, help_text='Author of the book.')
    description = models.TextField(blank=True, help_text='Description of the book.')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Price of the book.')
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='used',
        help_text='Condition of the book.'
    )
    published_date = models.DateField(null=True, blank=True, help_text='Publication date of the book.')
    image = models.ImageField(upload_to='book_images/', blank=True, null=True, help_text='Image of the book cover.')
    is_available = models.BooleanField(default=True, help_text='Whether the book is still available for sale.')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Time when the book was listed.')

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ['-created_at']
