import db_config


# db_params
connection = db_config.isDatabaseAvailable()
cursor = connection.cursor()

# csv_params
csv_dir = "csv_data"
csv_suicide_filename = "suicide-death-rates.csv"
csv_world_suicide = "world_suicide.csv"
