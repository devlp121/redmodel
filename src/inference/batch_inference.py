import os
import glob
import pandas as pd
import json
import uuid

import numpy as np
from fpdf import Template

from infer import _infer_example

cwd = os.getcwd()
filenames = glob.glob(cwd + "/*.csv")


def _load_csv_files(file_path):
    df_list = []
    print("Using file(s) from: ",file_path)
    for filename in file_path:
        df_list.append(pd.read_csv(filename, usecols=['text']))

    _combined_ds = pd.concat(df_list, ignore_index=True)

    return _combined_ds

def _make_batched_inference(files):
    _series_txt = _load_csv_files(filenames)

    _pred_list = []

    for value in _series_txt.values:
        pred, json = _infer_example(str(value))
        _pred_list.append(pred)
    prediction = _pred_list
    _insight(prediction)



    return prediction

def _insight(predictions):
    
    print("\nScores ABOVE zero indicate positive prediction of stress and negative values represent negative predictions\n")

    print('\nThe inference query shows a mean confidence of {} from {} instances\n'.format(
          np.mean(predictions), len(predictions)))
    
    print("A positive mean indicates a probable stress event or state")
    
    if np.mean(predictions) > 0:
        print("The mean is a positive integer")

    variance = np.var(predictions)
    print("\nVariance is; ",variance)

    minimum_score = np.min(predictions)
    print("\nMinimum value is:", minimum_score)
    
    maximum_score = np.max(predictions)
    print("\nMaximum value is: ", maximum_score)


u_value = str(uuid.uuid1())
print("Performing Inference ID:", u_value)

result_file = _make_batched_inference(filenames)