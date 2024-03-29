# Generated by Django 4.0.5 on 2024-03-07 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_vi', models.CharField(default='SOME STRING', max_length=50)),
                ('name_en', models.CharField(default='SOME STRING', max_length=50)),
                ('notes', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_html', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=45, null=True)),
                ('country_code', models.CharField(blank=True, max_length=4, null=True)),
                ('country_number', models.CharField(blank=True, max_length=4, null=True)),
                ('platform_number', models.CharField(blank=True, max_length=45, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('uid', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=9, max_digits=12, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=9, max_digits=12, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staffs_visible', models.BooleanField(default=True)),
                ('total_available_slot', models.IntegerField(blank=True, default=0, null=True)),
                ('total_available_slots_unit', models.CharField(blank=True, max_length=45, null=True)),
                ('total_bookings', models.IntegerField(blank=True, default=0, null=True)),
                ('opening_date', models.DateTimeField(blank=True, null=True)),
                ('avatar', models.JSONField(blank=True, default=dict, help_text='Avatar of merchant vio app', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('banner', models.JSONField(blank=True, default=dict, help_text='Banner', null=True)),
                ('allow_staff_connect_user', models.BooleanField(default=False)),
                ('note_placeholder', models.TextField(blank=True, help_text='Booking note for your client', null=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='merchants', to='product.category')),
                ('hashtags', models.ManyToManyField(blank=True, related_name='merchants', to='product.hashtag')),
                ('keywords', models.ManyToManyField(blank=True, related_name='merchants', to='product.keyword')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='merchants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(default=None, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_html', models.TextField(blank=True, null=True)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('images', models.JSONField(blank=True, default=list, null=True)),
                ('total_bookings', models.IntegerField(blank=True, default=0, null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sold_quantity', models.IntegerField(default=0, help_text='Product sold quantity')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
                ('hashtags', models.ManyToManyField(blank=True, related_name='products', to='product.hashtag')),
                ('keywords', models.ManyToManyField(blank=True, related_name='products', to='product.keyword')),
                ('merchant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.merchant')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_html', models.TextField(blank=True, null=True)),
                ('time', models.FloatField()),
                ('time_date', models.CharField(default=None, max_length=255, null=True)),
                ('require_staff', models.BooleanField(default=False)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('available_slots', models.IntegerField()),
                ('slots_unit', models.CharField(blank=True, max_length=50)),
                ('use_total_available_slots', models.BooleanField(default=False)),
                ('images', models.JSONField(blank=True, default=list, null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('flexible_time', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('total_bookings', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sold_quantity', models.IntegerField(blank=True, default=0, help_text='Service sold quantity', null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='product.category')),
                ('hashtags', models.ManyToManyField(blank=True, related_name='services', to='product.hashtag')),
                ('keywords', models.ManyToManyField(blank=True, related_name='services', to='product.keyword')),
                ('merchant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='product.merchant')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('discount', models.FloatField(blank=True, default=None, null=True)),
                ('unit', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, default=None, null=True)),
                ('type', models.CharField(blank=True, default='discount', max_length=255, null=True)),
                ('buy_quantity', models.IntegerField(blank=True, null=True)),
                ('get_quantity', models.IntegerField(blank=True, null=True)),
                ('images', models.JSONField(blank=True, default=list, null=True)),
                ('total_bookings', models.IntegerField(blank=True, default=0, null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('is_happy_hour', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('merchant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promotion', to='product.merchant')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(blank=True, related_name='promotions', to='product.product')),
                ('services', models.ManyToManyField(blank=True, related_name='promotions', to='product.service')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('merchant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='product.merchant')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='hashtag',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.hashtag'),
        ),
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='product.category'),
        ),
    ]
