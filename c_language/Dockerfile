FROM debian:bullseye-slim
WORKDIR /code

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    gdb \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*