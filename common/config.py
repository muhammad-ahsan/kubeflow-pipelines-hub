# The Kubeflow Pipeline SDK version should be >=1.6

import os

import google.cloud.aiplatform as aip
print('AI Platform version: {}'.format(aip.__version__))

PROJECT_ID = "ground-zero-377715"  # @param {type:"string"}
PROJECT_NUMBER="245954991926"
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

BUCKET_NAME = "ga-pipelines"  # @param {type:"string"}
BUCKET_URI = f"gs://ga-pipelines"
SERVICE_ACCOUNT = "sa-vertex-ai@ground-zero-377715.iam.gserviceaccount.com"  # @param {type:"string"}

PIPELINE_ROOT = f"{BUCKET_URI}/pipeline_root/minimal_pipeline"

# Initialite Vertex AI SDK
aip.init(project=PROJECT_ID, staging_bucket=BUCKET_URI)


