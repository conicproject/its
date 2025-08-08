import datetime
import random
import psycopg2


format = '%Y-%m-%d'
day_range = 31
car_type_range = 10
direction = {
    'in_bound': 'IN',
    'out_bound': 'OUT'
}
start_date = datetime.datetime.strptime('2022-08-01', format)

connection = psycopg2.connect(
    user="postgres",
    password="Abc@1234#",
    host="localhost",
    port="5432",
    database="development"
)

cursor = connection.cursor()

for day_idnex in range(day_range):
    date_ref = start_date + datetime.timedelta(days=day_idnex)

    insert_sql_command = """insert into records 
    (checkpoint_id, direction, car_type_id, volume, time_range_id, "date", created_at) values """

    for time_index in range(288):
        value = (time_index + 1) *5
        minute = value + random.randint(0, 3)
        sec = random.randint(0, 59)

        delta = datetime.timedelta(
            minutes=minute,
            seconds=sec
        )

        value_sql = "({}, '{}', {}, {}, {}, '{}', '{}'),"
        timestamp = date_ref + delta
        date_ = date_ref.strftime('%Y-%m-%d')
        created_at = datetime.datetime.strftime(timestamp, '%Y-%m-%d %H:%M:%S')

        for checkpoint_id in range(1, 28):
            for key in direction:
                dir = direction[key]

                for car_type_id in range(1, car_type_range + 1):
                    volume = random.randint(1, 100)
                    insert_data = value_sql.format(
                        checkpoint_id, dir, car_type_id, volume, time_index + 1, date_, created_at
                    )
                    
                    insert_sql_command += insert_data

    sql_command = insert_sql_command[:-1]

    cursor.execute(sql_command)
    connection.commit()