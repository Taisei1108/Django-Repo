from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.

class Daily(models.Model):
    date = models.DateField() #日付
    univ = MarkdownxField() #大学の課題とか
    study = MarkdownxField() #勉強したこと
    other = MarkdownxField() #その他
    first_meet = MarkdownxField() #初めて知ったこと
    wanna_do = MarkdownxField()#やりたいこと
    summary = MarkdownxField()#1日のまとめ
    evaluation = models.ForeignKey('Evaluation', on_delete=models.PROTECT) #1日の評価(外部キー)
    isOpen = models.BooleanField(default=True)#公開/非公開

    def __str__(self):
        date_str = self.date.strftime('%Y/%m/%d')
        return date_str


class Evaluation(models.Model):
    evaluation = models.CharField(max_length=255)

    def __str__(self):
        return self.evaluation