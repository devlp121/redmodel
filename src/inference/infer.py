from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import requests
import json
import os
import tempfile
import base64
import numpy as np
import pandas as pd

host = 'localhost'
port = '8501'

_inference_timeout = (50, 50)




def _infer_example(example):


    data = json.dumps( {"instances": [[example]]})
    
    server_url = 'http://' + host + ':' + port + '/v1/models/redmodel:predict'

    json_response = requests.post(server_url, data=data, timeout=_inference_timeout)
    json_response.raise_for_status()
    predictions = json.loads(json_response.text)['predictions']
    return predictions, json_response


