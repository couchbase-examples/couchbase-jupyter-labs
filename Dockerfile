FROM jupyter/base-notebook:notebook-7.0.6
LABEL author="Nithish Raghunandanan"
USER root
# Install the Couchbase SDK
RUN apt update && apt -y install build-essential libssl-dev libffi-dev python3-dev python3-pip python3-setuptools cmake git-all
RUN pip install couchbase python-dotenv
# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID
ENV JUPYTER_ENABLE_LAB=yes