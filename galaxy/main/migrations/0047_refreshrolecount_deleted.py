# NOTE(cutwater): This migration is replaced by v2_4_0 and should be
#   deleted once superseding migration is merged into master.
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20160930_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='refreshrolecount',
            name='deleted',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
