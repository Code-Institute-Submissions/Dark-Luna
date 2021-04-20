# Generated by Django 3.1.8 on 2021-04-20 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
                ('page', models.CharField(choices=[('Massage', 'Massage'), ('Sex Coaching', 'Sex Coaching'), ('Life Coaching', 'Life Coaching'), ('Shadow Work', 'Shadow Work'), ('Workshops', 'Workshops')], default='Massage', max_length=13)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
