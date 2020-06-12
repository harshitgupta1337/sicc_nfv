#!/bin/bash

# Now creating the other ports
docker run -d --privileged --name=src1 --net=none endpoint:latest tail -f /dev/null
docker run -d --privileged --name=src2 --net=none endpoint:latest tail -f /dev/null
docker run -d --privileged --name=dst --net=none endpoint:latest tail -f /dev/null

sudo ovs-docker add-port ovs-br1 eth0 src1 --ipaddress=192.168.1.2/24 --macaddress="00:00:00:00:00:01"
sudo ovs-docker add-port ovs-br1 eth0 src2 --ipaddress=192.168.2.2/24 --macaddress="00:00:00:00:00:02"
sudo ovs-docker add-port ovs-br2 eth0 dst --ipaddress=145.12.131.92/24 --macaddress="00:00:00:00:01:02"
# Adding routes on end hosts to be able to reach other endpoints
docker exec src1 route add -net 145.12.131.0/24  dev eth0
docker exec src2 route add -net 145.12.131.0/24  dev eth0
docker exec dst route add -net 192.168.1.0/24  dev eth0
docker exec dst route add -net 192.168.2.0/24  dev eth0
