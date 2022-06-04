from django.db import models

class Bar(models.Model):
    id = models.IntegerField(primary_key=True)
    unique_code = models.CharField(max_length=10, unique=True)

class Foo(models.Model):
    bar_code = models.ForeignKey(
        Bar, to_field="unique_code", db_column="bar_code", on_delete=models.CASCADE
    )
