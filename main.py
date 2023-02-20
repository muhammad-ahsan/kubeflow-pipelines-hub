
from common.compiler import compile_pipeline
from pipelines.string_manipulator import pipeline_string_manipulator


def main():
    pkg_path = 'artefacts/pipeline.json'
    compile_pipeline(pipeline_string_manipulator, pkg_path)
    print("Program executed successfully")

if __name__== "__main__":
    main()