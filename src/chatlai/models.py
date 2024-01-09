from django.db import models

# Create your models here.


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Lessons(BaseModel):

    title = models.CharField(max_length=250)
    lesson = models.TextField()
    publication_day = models.DateField()

    def __str__(self) -> str:
        return f'{self.title}'


class Examples(BaseModel):

    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    example = models.TextField()

    def __str__(self) -> str:
        return f'{self.lesson}'


class Keywords(BaseModel):

    keywords = models.JSONField()
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.keywords}'


    @property
    def validate_question(self, question: str) -> bool:
        if question in self.keywords:
            return True
        return False
