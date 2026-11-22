# Pinned to a dated Jupyter Docker Stacks build (Notebook 7.6.5 / JupyterLab 4.6.6 / Python 3.13).
# The old Docker Hub jupyter/* images stopped receiving updates in 2023; current builds live on quay.io.
FROM quay.io/jupyter/base-notebook:2026-11-16
LABEL author="Nithish Raghunandanan"
USER root
# Install the Couchbase SDK
RUN apt update && apt -y install build-essential libssl-dev libffi-dev python3-dev python3-pip python3-setuptools cmake git-all
RUN pip install couchbase python-dotenv
# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID
ENV JUPYTER_ENABLE_LAB=yes