# Building Kubeflow Pipelines 

This project is intended to be used as template for building new pipelines using Kubeflow.

# Repository Structure
```
/kubeflow-pipelines-hub
    ├── README.md
    ├── data
    │   ├── raw
    │   ├── processed
    │   └── ...
    ├── models
    │   ├── model1
    │   │   ├── train.py
    │   │   ├── predict.py
    │   │   └── ...
    │   ├── model2
    │   │   ├── train.py
    │   │   ├── predict.py
    │   │   └── ...
    │   └── ...
    ├── pipelines
    │   ├── pipeline1
    │   │   ├── pipeline.yaml
    │   │   └── ...
    │   ├── pipeline2
    │   │   ├── pipeline.yaml
    │   │   └── ...
    │   └── ...
    ├── components
    │   ├── feature_engineering
    │   │   ├── component.yaml
    │   │   ├── Dockerfile
    │   │   ├── src
    │   │   │   ├── ...
    │   │   └── ...
    │   ├── training
    │   │   ├── component.yaml
    │   │   ├── Dockerfile
    │   │   ├── src
    │   │   │   ├── ...
    │   │   └── ...
    │   └── ...
    ├── notebooks
    │   ├── exploration.ipynb
    │   ├── preprocessing.ipynb
    │   └── ...
    ├── scripts
    │   ├── data_preparation.py
    │   ├── evaluation.py
    │   └── ...
    ├── configs
    │   ├── config1.yaml
    │   ├── config2.yaml
    │   └── ...
    ├── tests
    │   ├── unit
    │   ├── integration
    │   └── ...
    └── ...
```