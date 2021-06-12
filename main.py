import misc
import csv_parser
import db_config
import graph_builder

connection = misc.connection
cursor = misc.cursor


def d_get_data_from_csv(csv_dir, csv_data) -> (list[dict], list[str]):
    countrylist = list()
    dataset = csv_parser.d_csv_dict_reader(csv_dir, csv_data)
    for item in dataset:
        country_name = list(item.keys())[0]
        if country_name not in countrylist:
            countrylist.append(country_name)
        else:
            continue
    return dataset, countrylist


# suicide_country_data, country_list = get_data_from_csv(misc.csv_dir, misc.csv_suicide_filename)
#
# for country in country_list:
#     db_config.isTableExists(connection, cursor, country.lower())

suicide_world_data, country_list = d_get_data_from_csv(misc.csv_dir, misc.csv_world_suicide)

world_population_data = csv_parser.p_csv_dict_reader_(misc.csv_dir, misc.csv_world_population)

for country in country_list:
    db_config.isTableExists(connection, cursor, country.lower())

Country = country_list[0]
for data in suicide_world_data:
    if list(data.keys())[0] == Country:
        db_config.updateSuicideData(connection, cursor, Country, **data[Country])

for data in world_population_data:
    db_config.updatePopulationData(connection, cursor, "world", **data)
