#!/bin/bash

sudo ovs-vsctl add-br ovs-br1
sudo ovs-vsctl add-br ovs-br2
sudo ovs-vsctl set bridge ovs-br1 other-config:datapath-id=0000000000000001
sudo ovs-vsctl set bridge ovs-br2 other-config:datapath-id=0000000000000002

sudo ovs-vsctl set-controller ovs-br1 tcp:192.168.56.2:6633
sudo ovs-vsctl set-controller ovs-br2 tcp:192.168.56.2:6633
# Preventing the OVS switch to enter standalone mode when the controller is down
sudo ovs-vsctl set-fail-mode ovs-br1 secure
sudo ovs-vsctl set-fail-mode ovs-br2 secure
sudo ovs-vsctl set bridge ovs-br1 protocols=OpenFlow13
sudo ovs-vsctl set bridge ovs-br2 protocols=OpenFlow13

# Now connecting the two switches together
sudo ovs-vsctl add-port ovs-br1 inter_sw_1 
sudo ovs-vsctl set interface inter_sw_1 type=patch

sudo ovs-vsctl add-port ovs-br2 inter_sw_2
sudo ovs-vsctl set interface inter_sw_2 type=patch

sudo ovs-vsctl set interface inter_sw_1 options:peer=inter_sw_2
sudo ovs-vsctl set interface inter_sw_2 options:peer=inter_sw_1

