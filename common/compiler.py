from typing import Callable
from kfp.v2 import compiler


def compile_pipeline(pipeline_func: Callable[[str, str], None], pkg_path: str):
    compiler.Compiler().compile(pipeline_func=pipeline_func, package_path=pkg_path)


