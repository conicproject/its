
from django.db import migrations
import os

class Migration(migrations.Migration):

    dependencies = [
        ('api', '00011_init_violation_record_config'),
    ]

    execute_path = os.getcwd()
    migration_sql_config = r'api/migrationSQL'
    migration_sql_path = os.path.join(execute_path, migration_sql_config)

    record_config = 'menu_name_config.sql'
    record_config_path = os.path.join(migration_sql_path, record_config)
    record_config_sql = open(record_config_path).read()

    operations = [
        migrations.RunSQL(record_config_sql)
    ]