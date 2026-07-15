FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    bc \
    build-essential \
    make \
    git \
    gdb \
    python3 \
    qemu-system-misc \
    gcc-riscv64-unknown-elf \
    binutils-riscv64-unknown-elf \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /xv6

COPY . .

CMD ["bash"]