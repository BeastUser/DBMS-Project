from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_bloodrequest_date'),  # Update this to match your latest migration
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TRIGGER set_created_at_trigger
            AFTER INSERT ON blood_stock
            BEGIN
                UPDATE blood_stock
                SET created_at = datetime('now')
                WHERE rowid = new.rowid;
            END;
            """
        ),
    ]
