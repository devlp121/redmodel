# The Redmodel User Guide

## Introduction

Redmodel is a machine learning model pipeline performing sentiment classification of stress on text data.

## Installation


```
bash setup_tfx_airflow.sh
```

The script install the development environment

```
bash airflow_config.sh
```
## Airflow DB Setup


```
airflow db init
```

Create an Admin role user then login into Airflow platform

## Initialize Airflow


```
airflow webserver
```

```
airflow scheduler
```



