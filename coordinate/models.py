from django.db import models
# from user.models import CustomUser
# Create your models here.
class Item(models.Model):
    CATEGORY_CHOICES = (
        ("tops", "トップス"),
        ("bottoms", "ボトムス"),
        ("onepiece", "ワンピース・セットアップ"),
        ("onepiece-tops", "ワンピース用カーディガン"),
        ("shoes", "シューズ"),
        ("hair", "ヘアアレンジ"),
    )

    SEASON_CHOICES = (
        ("spring", "春"),
        ("summer", "夏"),
        ("autumn", "秋"),
        ("winter", "冬"),
        ("all", "オール"),
    )
    
    name=models.CharField(
        verbose_name='名前',
        max_length=100
    )

    # user=models.ForeignKey(
    #     CustomUser,
    #     verbose_name='ユーザー',
    #     on_delete=models.CASCADE
    # )
    
    category=models.CharField(
        max_length=100,
        verbose_name='カテゴリー',
        choices=CATEGORY_CHOICES
    )
    
    season=models.CharField(
        max_length=100,
        verbose_name='季節',
        choices=SEASON_CHOICES
    )
    
    image=models.ImageField(
        upload_to='items/',
        verbose_name='写真',
        null=True,
        blank=True,
    )
    
    created_at=models.DateTimeField(
        verbose_name='新規更新日時',
        auto_now_add=True,
    )
    
    modified_at=models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True,
    )
    
    def __str__(self):
        return self.name
        