from kfp import dsl

from components.miscellaneous.lwp_components.string_ops import concat_op, reverse_op


@dsl.pipeline(name='text-transformer',
              description='A pipeline to concatenate two strings + reverse it')
def nlp_pipeline() -> str:
    concat_task: str = concat_op(a="first", b="second")
    reverse_task = reverse_op(a=concat_task.output)  # noqa
    return reverse_task.output  # noqa
