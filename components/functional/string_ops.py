import kfp

from kfp.v2.dsl import component

print(f"Kubeflow Pipeline SDK version: {kfp.__version__}")


@component(base_image='python:3.9')
def concat_op(a: str, b: str) -> str:
    return a + b


@component(base_image='python:3.9')
def reverse_op(a: str) -> str:
    return a[::-1]

