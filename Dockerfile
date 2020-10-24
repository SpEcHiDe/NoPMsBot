#  creates a layer from the base Docker image.
FROM python:3.8.5-slim-buster

WORKDIR /app

# https://shouldiblamecaching.com/
ENV PIP_NO_CACHE_DIR 1

# http://bugs.python.org/issue19846
# https://github.com/SpEcHiDe/PublicLeech/pull/97
ENV LANG C.UTF-8

# we don't have an interactive xTerm
ENV DEBIAN_FRONTEND noninteractive

# fix "ephimeral" / "AWS" file-systems
RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

# each instruction creates one layer
# Only the instructions RUN, COPY, ADD create layers.
# copies 'requirements', to inside the container
# ..., there are multiple '' dependancies,
# requiring the use of the entire repo, hence
# adds files from your Docker client’s current directory.
COPY . .

# install requirements, inside the container
RUN pip3 install --no-cache-dir -r requirements.txt

# specifies what command to run within the container.
CMD ["python3", "-m", "bot"]
