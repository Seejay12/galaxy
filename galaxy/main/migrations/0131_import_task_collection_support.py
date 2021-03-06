from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0130_move_collection_quality_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='importtask',
            name='collection',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='import_tasks',
                to='main.Collection'),
        ),
        migrations.AlterField(
            model_name='importtask',
            name='repository',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='import_tasks',
                to='main.Repository'),
        ),
    ]
