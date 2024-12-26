# CLUSTER-IN_DOCKER

This project sets up a Spark cluster using Docker and Docker Compose. The cluster includes a Spark master node and multiple Spark worker nodes. The setup also includes a shared workspace for data and scripts.

## Project Structure
command.txt: Contains commands for setting up and running the cluster.

spark-defaults.conf: Spark configuration file.

docker-compose.yml: Docker Compose file to set up the Spark cluster.

entrypoint.sh: Entrypoint script for the Docker containers.

hetzner-base.Dockerfile: Base Dockerfile for setting up the environment.

requirements.txt: Python dependencies.

spark-cluster.Dockerfile: Dockerfile for Spark master and worker nodes.

spark.py: Spark job script for analyzing Uber data.

uber_data.csv: Uber dataset.

uber_analysis_result.csv: Directory for storing analysis results.



## Prerequisites

- Docker
- Docker Compose

## Setup

1. Build the Docker images and start the cluster:

    ```sh
    docker-compose build
    docker-compose up -d
    ```

2. Access the Spark master container:

    ```sh
    docker exec -it spark-master /bin/bash
    ```

3. Submit the Spark job:

    ```sh
    /opt/spark/bin/spark-submit --master spark://spark-master:7077 /opt/workspace/spark.py
    ```

4. Stop the cluster:

    ```sh
    docker stop spark-worker-1
    docker stop spark-worker-2
    docker stop spark-master
    docker-compose down
    ```

## Configuration

- [spark-defaults.conf](http://_vscodecontentref_/9): Spark configuration file.
- [requirements.txt](http://_vscodecontentref_/10): Python dependencies.

## Dockerfiles

- [hetzner-base.Dockerfile](http://_vscodecontentref_/11): Base Dockerfile for setting up the environment.
- [spark-cluster.Dockerfile](http://_vscodecontentref_/12): Dockerfile for Spark master and worker nodes.

## Scripts

- [entrypoint.sh](http://_vscodecontentref_/13): Entrypoint script for the Docker containers.
- [spark.py](http://_vscodecontentref_/14): Spark job script for analyzing Uber data.

## Data

- [uber_data.csv](http://_vscodecontentref_/15): Uber dataset.
- `workspace/uber_analysis_result.csv`: Directory for storing analysis results.

## License

This project is licensed under the MIT License.