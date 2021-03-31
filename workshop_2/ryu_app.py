from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet.packet import Packet
from ryu.lib.packet.ethernet import ethernet
from ryu.lib.packet.arp import arp
from ryu.ofproto import ether
from ryu.lib.mac import haddr_to_bin
from workshop_parent import WorkshopParent

NF_MACS = ["00:00:00:00:02:01", "00:00:00:00:02:02"]
SRC_MAC = "00:00:00:00:01:01"
DST_MAC = "00:00:00:00:01:02"

SRC_IP = "192.168.1.2"
DST_IP = "145.12.131.92"
NF_IN_PORT = 3
NF_OUT_PORT = 4
SRC_PORT = 1
DST_PORT = 2

class Workshop2(WorkshopParent):
    def __init__(self, *args, **kwargs):
        super(Workshop2, self).__init__(*args, **kwargs)

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
