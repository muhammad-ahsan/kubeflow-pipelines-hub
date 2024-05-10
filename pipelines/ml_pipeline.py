from kfp import dsl
from kfp.dsl import ContainerSpec


@dsl.container_component
def data_quality_op() -> ContainerSpec:
    return ContainerSpec(
        image='data-quality-image:latest',
        command=['python', 'main.py'],
    )


@dsl.pipeline(
    name='ml_pipeline',
    description='An end-to-end machine learning pipeline'
)
def ml_pipeline():
    dq_op = data_quality_op()
