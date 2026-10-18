FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    clang \
    libc++-dev \
    libc++abi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m student
WORKDIR /app
RUN chown student:student /app
#USER student