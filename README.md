# CLUSTER-IN_DOCKER

This project sets up a Spark cluster using Docker and Docker Compose. The cluster includes a Spark master node and multiple Spark worker nodes. The setup also includes a shared workspace for data and scripts.

## Project Structure
```
cluster/
        ├── command.txt 
        ├── conf/ │ 
            └── spark-defaults.conf 
        ├── docker-compose.yml 
        ├── entrypoint.sh 
        ├── hetzner-base.Dockerfile 
        ├── requirements/ 
            │ └── requirements.txt 
        ├── spark-cluster.Dockerfile 
        └── workspace/ 
            ├── pycache/ 
            ├── spark.py 
            ├── uber_analysis_result.csv/ 
            ├── uber_data.csv
```


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