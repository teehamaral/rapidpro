# Generated by Django 2.1.5 on 2019-03-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("channels", "0117_auto_20190227_2137")]

    operations = [
        migrations.AlterField(
            model_name="channelevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("unknown", "Unknown Call Type"),
                    ("mt_call", "Outgoing Call"),
                    ("mt_miss", "Missed Outgoing Call"),
                    ("mo_call", "Incoming Call"),
                    ("mo_miss", "Missed Incoming Call"),
                    ("stop_contact", "Stop Contact"),
                    ("new_conversation", "New Conversation"),
                    ("referral", "Referral"),
                    ("welcome_message", "Welcome Message"),
                ],
                help_text="The type of event",
                max_length=16,
                verbose_name="Event Type",
            ),
        )
    ]
