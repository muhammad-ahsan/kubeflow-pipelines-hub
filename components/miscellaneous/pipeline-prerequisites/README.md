# Container Components
- Create a component via an arbitrary container definition. 
- Can be written in any programming language 
- Containerized application can be plugged into Kubeflow pipeline 


## Pipeline Prerequisites

### Overview
This Python-based application serves as a critical first component in the Kubeflow pipeline. It checks all the necessary dependencies required for a Kubeflow pipeline to execute smoothly. By running a single Python script as a Docker container, it ensures that all prerequisites are met before initiating the pipeline execution. This proactive approach saves valuable time and resources by detecting and addressing any missing prerequisites at the earliest stage of the pipeline.

## Features
- **Prerequisite Verification**: The application checks for all required dependencies and prerequisites before proceeding with the Kubeflow pipeline execution.
- **Single Script Execution**: Running a single Python script as a Docker container simplifies deployment and ensures consistency across different environments.
- **Resource Optimization**: By identifying missing prerequisites early in the process, the application helps optimize resource utilization by preventing unnecessary pipeline executions.

**Output**:
- If all prerequisites are satisfied, the application will indicate successful verification.
- If any prerequisite is missing, the application will alert and prevent the Kubeflow pipeline execution.


## Usage
**Building the Docker Image**:

```
docker build -t <REGISTRY>/pipeline-prerequisites:<TAG> .
```

**Building the Docker Image**:

```
docker push <REGISTRY>/pipeline-prerequisites:<TAG>
```
## Configuration
- **Dependency Definitions**: Prerequisites and dependencies are defined in an external YAML file (`dependencies.yaml`). You can customize this file to include additional checks or modify existing ones as needed.

## Contributing
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to help improve this project.

## License
This project is licensed under the [MIT License](LICENSE).