from kfp import dsl, components
from kfp.dsl import ContainerSpec


@dsl.container_component
def pipeline_prerequisites_op() -> ContainerSpec:
    return ContainerSpec(
        image='pipeline-prerequisites:latest',
        command=['python', 'main.py'],
    )


data_quality_comp = components.load_component_from_file(
    'components/data-quality/component.yaml')


@dsl.pipeline(
    name='ml_pipeline',
    description='An end-to-end machine learning pipeline'
)
def ml_pipeline():
    dependency_check = pipeline_prerequisites_op()
    data_quality = data_quality_comp()
