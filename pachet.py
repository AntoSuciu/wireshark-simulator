import json

class Pachet:
    def __init__(self, eth_dst, eth_src, IP_dst, IP_src, IP_vers, IP_proto,
                 TCP_sport, TCP_dport, UDP_sport, UDP_dport):
        self.eth_dst = eth_dst
        self.eth_src = eth_src
        self.IP_dst = IP_dst
        self.IP_src = IP_src
        self.IP_vers = IP_vers
        self.IP_proto = IP_proto
        self.TCP_sport = TCP_sport
        self.TCP_dport = TCP_dport
        self.UDP_sport = UDP_sport
        self.UDP_dport = UDP_dport

    def __str__(self):

        json_string = '{{"Ethernet":' \
                      '         {{"src":"{}",' \
                      '           "dst":"{}"}},' \
                      '"IP":{{"src":"{}",' \
                      '       "dst":"{}",' \
                      '       "version":"{}",' \
                      '       "proto":"{}"}},' \
                      '"TCP":{{"sport":"{}",' \
                      '        "dport":"{}"}},' \
                      '"UDP":{{"sport":"{}",' \
                      '"dport":"{}"}}}}'.format(
            self.eth_src, self.eth_dst, self.IP_src, self.IP_dst, self.IP_vers, self.IP_proto, self.TCP_sport,
            self.TCP_dport, self.UDP_sport, self.UDP_dport)


        json_python_object = json.loads(json_string)
        json_python_object = json.dumps(json_python_object, indent=2)
        return json_python_object

