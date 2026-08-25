from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="technology",
            name="slug",
            field=models.SlugField(
                blank=True,
                max_length=120,
            ),
        ),
    ]