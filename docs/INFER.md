# The Inference Guide

## Initialize docker container serving the saved model

Open script and set the path to saved model directory

```
bash docker_run.sh
```
Run inference script for batched inference with input CSV in the working directory.

#### _Ensure the input file contains a column name "text" which contains examples to be predicted_


```
python batched_inference.py
```
## Send email output
#### _Setup SMTP Server_


```
python output.py [arguments: -r {receipient}, -s{sender}]


python output.py -r example@model.com -s infer@redmodel.com
```


