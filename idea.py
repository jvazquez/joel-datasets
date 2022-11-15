from typing import Dict

dataset = [
    (1, "Mar del Plata"),
    (2, "Constiucion"),
    (3, "Mar del Plata")
]


def run(df) -> Dict:
    accumulator = {}

    for value in df:
        print(value)
    # for _id, city_name in dataset:
    #     if city_name not in accumulator.keys():
    #         accumulator[city_name] = [_id]
    #     else:
    #         accumulator[city_name].append(_id)
    # 
    # return accumulator


if __name__ == "__main__":
    print(run())
