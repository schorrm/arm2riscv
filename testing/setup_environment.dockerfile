FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install -y python3-pip gcc-aarch64-linux-gnu gcc-riscv64-linux-gnu
ADD https://github.com/schorrm/arm2riscv/raw/master/testing/qemu_binaries/qemu-aarch64-static /usr/local/bin/
ADD https://github.com/schorrm/arm2riscv/raw/master/testing/qemu_binaries/qemu-riscv64-static /usr/local/bin/
RUN chmod 755 /usr/local/bin/qemu-aarch64-static /usr/local/bin/qemu-riscv64-static
RUN pip3 install lark-parser tqdm
