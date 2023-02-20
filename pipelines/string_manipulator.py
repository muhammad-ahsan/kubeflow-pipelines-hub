import kfp 
from kfp.v2 import dsl
from kfp.v2.dsl import component
from typing import NamedTuple


print(f"Kubeflow Pipeline SDK version: {kfp.__version__}")


import common.config as config

@component
def concat_op(a: str, b: str) -> str:
    return a + b

@component
def reverse_op(a: str) -> NamedTuple("outputs", [("before", str),("after", str)]):
    return a, a[::-1]


@dsl.pipeline(name='string-manipulator', description='A pipeline to concatenate two strings and finally reverse it')
def pipeline_string_manipulator(first_string: str = 'muhammad', second_string: str = 'ahsan'):
    concat_task = concat_op(first_string, second_string) 
    reverse_task = reverse_op(concat_task.output)
