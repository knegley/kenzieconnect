# Generated by Django 3.1.2 on 2020-10-10 14:27

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_pet', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Dogs and Cats', 'Dogs and Cats'), ('No Pets', 'No Pets')], max_length=60)),
                ('question_food', models.BooleanField()),
                ('question_date', models.CharField(choices=[('Late-nighter', 'Late-nighter'), ('Early Evening', 'Early Evening'), ('Weekend Afternoon', 'Weekend')], max_length=50)),
                ('question_activity', models.CharField(choices=[('PS5', 'PS5'), ('Dungeons and Dragons ', 'Dungeons and Dragons'), ('Hackathon', 'Hackathon'), ('Dinner', 'Dinner')], max_length=50)),
                ('question_star', models.CharField(choices=[('Darth Vader', 'Darth Vader'), ('LukeSky Walker', 'Luke Skywalker'), ('Han Solo', 'Han Solo'), ('Princess Leia', 'Princess Leia'), ('Padme Amidala', 'Padme Amidala'), ('Jyn Ersp', 'Jyn Ersp'), ('Yoda', 'Yoda'), ('Chewbacca', 'Chewbacca'), ('Jar Jar Binks', 'Jar Jar Binks')], max_length=50)),
                ('question_booze', models.CharField(choices=[('Beer', 'Beer'), ('Wine', 'Wine'), ('Cocktails', 'Cocktails'), ('No Alcohol Please', 'No Alcohol Please')], max_length=50)),
                ('question_pjs', models.CharField(choices=[('Never', 'Never'), ('100% Yes', '100% Yes'), ('Business on top, pjs on bottom', 'Business on top, pjs on bottom'), ('Literally took them off 1 min ago', 'Literally took them off 1 min ago')], max_length=50)),
                ('question_sleep', models.CharField(choices=[('Early Bird', 'Early Bird'), ('Night Owl', 'Night Owl')], max_length=10)),
                ('question_mind', models.CharField(choices=[('Cheeky Child', 'Cheeky Child'), ('Tormented Teenager', 'Tormented Teenager'), ('Mad Mid-lifer', 'Mad Mid-lifer'), ('Groovy Grandparent', 'Groovy Grandparent')], max_length=50)),
                ('question_dog', models.CharField(choices=[('Jack Russell – small, tough, opinionated', 'Jack Russell – small, tough, opinionated'), ('Tibetan Mastiff – or some other very rare breed', 'Tibetan Mastiff – or some other very rare breed'), ('German Shepherd – poised and elegant but rather hardy', 'German Shepherd – poised and elegant but rather hardy'), ('Poodle – beautifully presented but a bit of a poser', 'Poodle – beautifully presented but a bit of a poser'), ('Golden Retriever – warm, cuddly and great with children', 'Golden Retriever – warm, cuddly and great with children'), ('Pit Bull Terrier – scary but kind deep down', 'Pit Bull Terrier – scary but kind deep down'), ('Labradoodle – or some other cute hybrid', 'Labradoodle – or some other cute hybrid')], max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('NonBinary', 'NonBinary'), ('Other', 'Other')], max_length=20)),
                ('bio', models.CharField(max_length=1000)),
                ('sexual_preference', models.CharField(choices=[('Straight', 'Straight'), ('Gay', 'Gay'), ('Bisexual', 'Bisexual'), ('Other', 'Other')], max_length=20)),
                ('email', models.EmailField(max_length=150)),
                ('displayname', models.CharField(max_length=60)),
                ('survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='survey_data', serialize=False, to='kenzie_connect.survey')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Penpal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penpal_message', models.CharField(max_length=500)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_fk', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kenzie_connect.penpal')),
                ('notification_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]