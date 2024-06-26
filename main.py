import logging
import os
import importlib
import pkgutil

import kfp
from kfp import compiler, local

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Kubeflow Pipeline SDK version: {kfp.__version__}")


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


def main(pipeline_name: str = "ml_pipeline", env: str = "local", ):
    artifact_registry: str = 'artifacts/'
    if not os.path.exists(artifact_registry):
        os.makedirs(artifact_registry)

    package_path = artifact_registry + 'pipeline.json'

    # Set up compute environment
    if env == "local":
        # SubprocessRunner only supports running Lightweight Python Components
        local.init(runner=local.DockerRunner())
    else:
        raise EnvironmentError("Remote k8s environment is not supported yet.")

    # Load pipeline definition
    custom_pipeline = fetch_pipeline(pipeline_name)

    # Compile the pipeline
    compiler.Compiler().compile(pipeline_func=custom_pipeline,
                                package_path=package_path)
    # Triggering pipeline
    _ = custom_pipeline()


if __name__ == "__main__":
    main()
