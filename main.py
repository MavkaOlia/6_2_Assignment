import csv
from convertor.temperature import cel_to_fahr, fahr_to_cel


def convert_temperature(input_file, output_file, target_unit):
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    for row in rows:
        temperature_reading = float(row['Reading'][:-2])  
        if 'C' in row['Reading']:
            converted_temperature = cel_to_fahr(temperature_reading) if target_unit == 'F' else temperature_reading
        else:
            converted_temperature = fahr_to_cel(temperature_reading) if target_unit == 'C' else temperature_reading

        row['Reading'] = f'{converted_temperature}°{target_unit}'

    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ['Date', 'Reading']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
