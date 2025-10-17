# Use micromamba (lightweight conda)
FROM mambaorg/micromamba:1

# Allow use of the base env in RUN and CMD
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# Set workdir for notebooks
WORKDIR /srv/notebooks

# Install Python + JupyterLab
RUN micromamba install -y -n base -c conda-forge \
      python=3.11 jupyterlab=4 ipykernel \
    && micromamba clean -a -y

# Set default environment variables
ENV JUPYTER_TOKEN=changeme \
    JUPYTER_PORT=8888

EXPOSE 8888

# Use micromamba's shell hook to activate base env automatically
# before launching Jupyter
CMD ["bash", "-lc", "micromamba run -n base jupyter lab \
  --ip=0.0.0.0 \
  --port=${JUPYTER_PORT} \
  --no-browser \
  --ServerApp.token=${JUPYTER_TOKEN} \
  --ServerApp.allow_remote_access=1 \
  --ServerApp.root_dir=/srv/notebooks"]
