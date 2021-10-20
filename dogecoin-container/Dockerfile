FROM ubuntu:20.04

# dogecoin Core realese version
ARG doge_version=1.14.4

# install updates
RUN apt update && apt upgrade -y 

# install depends
RUN apt install -y wget gpg ca-certificates tar dirmngr

# download realese tarball && unarhive && remove tarball 
RUN wget -O dogecoin.tar.gz https://github.com/dogecoin/dogecoin/releases/download/v${doge_version}/dogecoin-${doge_version}-x86_64-linux-gnu.tar.gz && tar -xf dogecoin.tar.gz && rm dogecoin.tar.gz

# install to /usr/bin/
RUN install -m 755 -o root -g root -t /usr/bin dogecoin-${doge_version}/bin/*

# start dogecoind and expose p2p port
CMD ["dogecoind"]
EXPOSE 22556

LABEL name="dogecoin-container" dogecoin-version="${doge_version}" description="Dogecoin container"


# 1.Напишите Dockerfile для сборки данного проекта:
# https://github.com/dogecoin/dogecoin

