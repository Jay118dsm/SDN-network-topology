#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.node import Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.node import RemoteController
from mininet.term import makeTerm
import sys


def myTopo():
    net = Mininet( topo=None, autoSetMacs=True, build=False, ipBase='10.0.1.0/24')
    
    c1 = net.addController('c1',RemoteController)
    
    client = net.addHost('client', cls=Host, defaultRoute=None)
    server1 = net.addHost('server1', cls=Host, defaultRoute=None)
    server2 = net.addHost('server2', cls=Host, defaultRoute=None)
    
    switch = net.addSwitch('s1', cls=OVSKernelSwitch, protocols="OpenFlow13")

    # Add links
    net.addLink(client, switch)
    net.addLink(server1, switch)
    net.addLink(server2, switch)
    
    net.build()
    
    client.setMAC(intf="client-eth0",mac="00:00:00:00:00:03")
    server1.setMAC(intf="server1-eth0",mac="00:00:00:00:00:01")
    server2.setMAC(intf="server2-eth0",mac="00:00:00:00:00:02")
    
    client.setIP(intf="client-eth0",ip='10.0.1.5/24')
    server1.setIP(intf="server1-eth0",ip='10.0.1.2/24')
    server2.setIP(intf="server2-eth0",ip='10.0.1.3/24')
    
    net.start()
    
    net.terms += makeTerm(c1)
    net.terms += makeTerm(client)
    net.terms += makeTerm(server1)
    net.terms += makeTerm(server2)

    CLI(net)
    net.stop()
    
if __name__=='__main__':
    setLogLevel('info')
    myTopo()















