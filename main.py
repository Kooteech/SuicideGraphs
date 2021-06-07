import misc
import csv_parser
import db_config

connection = misc.connection
cursor = misc.cursor


def get_data_from_csv(csv_dir, csv_data) -> (list[dict], list[str]):
    countrylist = list()
    data = csv_parser.csv_dict_reader(csv_dir, csv_data)
    for item in data:
        country_name = list(item.keys())[0]
        if country_name not in countrylist:
            countrylist.append(country_name)
        else:
            continue
    return data, countrylist


# suicide_country_data, country_list = get_data_from_csv(misc.csv_dir, misc.csv_suicide_filename)
#
# for country in country_list:
#     db_config.isTableExists(connection, cursor, country.lower())

suicide_world_data, country_list = get_data_from_csv(misc.csv_dir, misc.csv_world_suicide)

for country in country_list:
    db_config.isTableExists(connection, cursor, country.lower())

Country = country_list[0]
for data in suicide_world_data:
    if list(data.keys())[0] == Country:
        db_config.updateData(connection, cursor, Country, **data[Country])