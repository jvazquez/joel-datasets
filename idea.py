import csv
import resource

from os.path import abspath, dirname, join
from os import listdir
from typing import Dict, Set


def csv_content(filename: str) -> Dict[str, Set]:
    file_data = []
    with open(filename, "r") as content:
        csv_reader = csv.reader(content)
        # I don't care about the header
        next(csv_reader)
        for row in csv_reader:
            station_name = row[5]
            station_id = row[6]
            if (
                    len(station_name) > 0 and
                    station_name != "nan" and
                    len(station_id) > 0 and
                    station_id != "nan"
            ):
                file_data.append((row[5], row[6],))
    file_data.sort(key=lambda a: a[1])
    # Extract the unique names
    unique_station_names = {
        station_name for station_id, station_name in
        file_data
    }
    station_names = list(unique_station_names)
    station_names.sort()
    # Create a hashmap (a key value data type), where I use
    # {str: set}. We use set because we don't care about repeated station ids,
    # we want the different ids the users give
    station_map = {station_name: set() for station_name in station_names}

    for station_id, station_name in file_data:
        station_map[station_name].add(station_id)

    yield station_map


if __name__ == "__main__":
    data_path = join(dirname(abspath(__file__)), "data")
    csv_files = [
        join(data_path, csvfile) for csvfile in
        filter(lambda x: x.endswith("csv"), listdir(data_path))
    ]

    different_data = []
    for csv_file in csv_files:
        for result in csv_content(csv_file):
            different_data.append(result)

    print("All files opened, now you have a listing of "
          f"{len(different_data)} files condensed")
    """
    different_data contains a List of Dictionaries that contain a string and
    a set
    For example
    [
        {
            'Wilton Ave & Diversey Pkwy': {'TA1305000039', '13084',
            'TA1309000023', '13323', 'TA1309000036', '13290', 'TA1306000007',
            '13434', 'TA1307000166', '13135', 'TA1306000026',
            'TA1305000014', 'TA1307000150', 'TA1307000136',
            'TA1305000030', ...}
        }
    ]

    A single file, gives these values
    Generator mode for a single file
    Peak memory usage=5.878883361816406 MB
    User mode time=25.02058
    System mode time=8.552199
    """
    print("Peak memory usage="
          f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2} MB")
    print(f"User mode time={resource.getrusage(resource.RUSAGE_SELF).ru_utime}")
    print("System mode time"
          f"={resource.getrusage(resource.RUSAGE_SELF).ru_stime}")