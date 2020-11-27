import os
import json
import pandas as pd


def read_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


def read_all_json_files(JSON_ROOT):
    for direpath, direnames, filenames in os.walk(JSON_ROOT):
        result = []
        for file in filenames:
            if file.endswith('.json'):
                json_content = read_json(os.path.join(JSON_ROOT, file))
                for index in json_content["results"]:
                    index["source"] = file
                    result.append(index)
        df_loc = pd.DataFrame(result)
        return df_loc
