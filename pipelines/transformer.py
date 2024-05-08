from kfp import dsl

from components.functional.string_ops import concat_op, reverse_op


@dsl.pipeline(name='text-transformer',
              description='A pipeline to concatenate two strings + reverse it')
def custom_pipeline(input_1: str, input_2: str) -> str:
    concat_task: str = concat_op(a=input_1,
                                 b=input_2)
    reverse_task = reverse_op(a=concat_task.output)  # noqa
    return reverse_task.output  # noqa
