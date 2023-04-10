from django.db import models


class Todo(models.Model):
    title = models.CharField('Название', max_length=100)
    is_complete = models.BooleanField('Выполнено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self) -> str:
        return f'{self.title} {self.is_complete}'
