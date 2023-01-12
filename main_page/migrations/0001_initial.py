# Generated by Django 4.1.5 on 2023-01-07 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_price', models.FloatField()),
                ('course_period', models.FloatField()),
                ('course_description', models.TextField()),
                ('course_photo', models.ImageField(upload_to='')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('course_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_start_date', models.DateField()),
                ('sale_end_date', models.DateField()),
                ('courses', models.ManyToManyField(to='main_page.course')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.course')),
            ],
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('user_courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.course')),
            ],
        ),
    ]
