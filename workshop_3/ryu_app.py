from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet.packet import Packet
from ryu.lib.packet.ethernet import ethernet
from ryu.lib.packet.arp import arp
from ryu.ofproto import ether

import sys
sys.path.append("../workshop_2/")
from workshop_parent import WorkshopParent

# Description of traffic endpoints for the Network Function 
'''
DST = {
    "IN_MAC" : "",
    "IN_PORT" : ,
    "IP" : ""
}

SRC = {
    "OUT_MAC" : "",
    "OUT_PORT" : ,
    "IP" : ""
}
'''
# Description of NF instances
# NF Instance 1
NF_1 = {
    "IN_MAC" : "",
    "OUT_MAC" : "",
    "SWITCH_DPID" : ,
    "IN_PORT" : ,
    "OUT_PORT" : 
}

# NF Instance 2
NF_2 = {
    "IN_MAC" : "",
    "OUT_MAC" : "",
    "SWITCH_DPID" : ,
    "IN_PORT" : ,
    "OUT_PORT" : 
}

# Pool of NF Instances
NF_POOL = [NF_1, NF_2]

class Workshop4(WorkshopParent):

    def __init__(self, *args, **kwargs):
        super(Workshop4, self).__init__(*args, **kwargs)
        print ("Initializing RYU controller app for Workshop 4")

    # Function to handle packets belonging to ARP protocol
    def handle_arp(self, datapath, packet, ether_frame, in_port):
        arp_packet = packet.get_protocol(arp)

        if arp_packet.opcode == 1: # Send an ARP Response for the incoming Request
            # Determine the MAC Address for IP Address being looked up
            # Determine the out port to send the ARP Response 

            ''' Your code here '''

            # Call helper function to create and send ARP Response
            self.send_arp_reply(datapath, src_mac, src_ip, dst_mac, dst_ip, out_port)
        else:
            # We don't expect to receive ARP replies, so do nothing
            pass

    # Function to handle non-ARP packets
    def handle_packet(self, msg):
        ''' Your code here '''
