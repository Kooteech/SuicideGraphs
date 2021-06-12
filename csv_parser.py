import csv


# Entity,Code,Year,Rate

def d_csv_dict_reader(csv_dir, filename) -> list:
    data_list = list()
    tmp_dict = dict()
    file_obj = open(f"{csv_dir}\\{filename}")
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        data_list.append({line['Country']: {'Year': line['Year'], 'Rate': line['Rate']}})
    file_obj.close()
    return data_list


def p_csv_dict_reader_(csv_dir, filename) -> list:
    data_list = list()
    tmp_dict = dict()
    file_obj = open(f"{csv_dir}\\{filename}")
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        data_list.append({'Year': line['Year'], 'Population': line['Population']})
    file_obj.close()
    return data_list
