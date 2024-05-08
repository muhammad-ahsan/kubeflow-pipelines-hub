import logging
import os
import importlib
import pkgutil

from kfp import compiler, local

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_pipeline(func_name):
    try:
        package = importlib.import_module("pipelines")
        for loader, module_name, is_pkg in pkgutil.walk_packages(package.__path__):
            if not is_pkg:
                module = importlib.import_module(f"pipelines.{module_name}")
                if hasattr(module, func_name) and callable(getattr(module, func_name)):
                    return getattr(module, func_name)
        print(f"No callable function named '{func_name}' found in modules within the 'pipelines' package.")
    except ModuleNotFoundError:
        pass
    raise ModuleNotFoundError("Package 'pipelines' not found.")


def main(pipeline_name: str = "custom_pipeline", env: str = "local-docker", ):
    artifact_registry: str = 'artifacts/'
    if not os.path.exists(artifact_registry):
        os.makedirs(artifact_registry)
    # Set up compute environment
    if env == "local":
        local.init(runner=local.SubprocessRunner())
    elif env == "local-docker":
        local.init(runner=local.DockerRunner())
    else:
        raise EnvironmentError("Remote k8s environment is not supported yet.")

    # Load pipeline definition
    my_pipeline = fetch_pipeline(pipeline_name)

    # Compile the pipeline
    package_path = artifact_registry + 'pipeline.json'
    compiler.Compiler().compile(pipeline_func=my_pipeline,
                                package_path=package_path)

    # Executing pipeline
    pipeline_task = my_pipeline(input_1="x", input_2="y")
    logger.info(pipeline_task.output)
    logger.info("Pipeline execution is successful.")


if __name__ == "__main__":
    main()
