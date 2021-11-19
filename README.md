# Couchbase Jupyter Labs

A series of labs created to start using Couchbase with the Python SDK. It includes the following labs:

- Introduction to Couchbase
- Key Value Operations
- Indexing
- N1QL Querying
- Full Text Search

## Running the Labs Using Docker Compose

### Prerequisites

- [Docker & Docker Compose](https://docs.docker.com/compose/install/)

To bring up the Couchbase and the Jupyter Lab environment with the Couchbase Python SDK, run

`docker-compose up`

Access the Jupyter Lab environment by clicking on the access URL in the logs as shown in the screenshot below.

![access-jupyter-lab](notebooks/img/access_jupyter_lab.png)

Couchbase can be accessed on
http://localhost:8091/

Note that it might take a few minutes to start Couchbase.

Follow the instructions in [Lab 1](notebooks/Lab_01_Introduction_to_Couchbase.ipynb)

Follow the rest of the labs sequentially.

## Running the Labs Locally

### Prerequisites

- Python 3.8 or higher

- Install the Couchbase SDK & Jupyter Lab

  `pip install couchbase jupyterlab`

- Running Couchbase using Docker

  `docker run -d --name db -p 8091-8094:8091-8094 -p 11210:11210 couchbase`

## Building Docker Image with Jupyter Lab & Couchbase SDK

`docker build -t couchbase-jupyter-lab .`

Running the Image
`docker run -p 8888:8888 -v $(pwd):/home/jovyan/work -it couchbase-jupyter-lab`

Click on the link to access Jupyter lab from the container logs as shown in the screenshot above.
