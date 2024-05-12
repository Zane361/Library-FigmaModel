from django.db import models
from random import sample
import string

class CodeGenerate(models.Model):
    code = models.CharField(max_length=255, blank=True,unique=True)
    
    @staticmethod
    def generate_code():
        return ''.join(sample(string.ascii_letters + string.digits, 15)) 
    

    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                code = self.generate_code()
                if not self.__class__.objects.filter(code=code).count():
                    self.code = code
                    break
        super(CodeGenerate,self).save(*args, **kwargs)


    class Meta:
        abstract = True


class Category(CodeGenerate):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/')


class Author(CodeGenerate):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='author/')
    birth = models.DateField()
    birth_place = models.CharField(max_length=255)
    death = models.DateField(blank=True, null=True)
    death_place = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField()
    work = models.TextField()

    @property
    def books(self):
        return Book.objects.filter(author=self)


class Book(CodeGenerate):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.DateField()
    pages = models.IntegerField()
    publisher = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='book-image/')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    has_audio = models.BooleanField()
    audio_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    if not has_audio:
        audio_price = 0
    has_electron = models.BooleanField()
    electron_types = models.TextField(blank=True, null=True)
    electron_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
    if not has_electron:
        electron_types = None
        electron_price = 0

    @property
    def quotes(self):
        return Quote.objects.filter(book=self)
    
    @property
    def reviews(self):
        return Review.objects.filter(book=self)
    

class Quote(CodeGenerate):
    quote = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Review(CodeGenerate):
    body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    mark = models.IntegerField()


