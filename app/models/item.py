from django.db.models import Model, CharField, TextField, DateTimeField


class Item(Model):
    name = CharField(max_length=255)
    description = TextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "app"

    def __str__(self) -> str:
        return self.name
