from typing import Dict, Union

from kfp import dsl
from kfp.dsl import ContainerSpec

from utils.parse_args import parse_args_to_dict


@dsl.container_component
def data_quality_op() -> ContainerSpec:
    return ContainerSpec(
        image='data-quality-image:latest',
        command=['python', 'main.py'],
    )


@dsl.pipeline(
    name='Machine Learning Pipeline',
    description='An end-to-end machine learning pipeline'
)
def ml_pipeline():
    # **kwargs: Dict[str, Union[int, str]]
    # kwargs = None
    # args = parse_args_to_dict(**kwargs)
    dq_op = data_quality_op()
