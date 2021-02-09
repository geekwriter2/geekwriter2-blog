# Generated by Django 3.1.5 on 2021-02-06 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_auto_20210206_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogging.category')),
                ('admin_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogging.post')),
            ],
        ),
    ]