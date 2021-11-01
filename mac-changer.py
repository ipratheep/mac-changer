
import subprocess
import optparse
import re

print("***********************************")
print("*                                 *")
print("*                                 *")
print("*          Mac changer            *")
print("*                                 *")
print("*                                 *")
print("***********************************")


def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter interface i.e = eth0")
    parser.add_option("-m", dest="mac_address", help="Enter mac address i.e = xx:xx:xx:xx:xx:xx")
    (options, arguments) = parser.parse_args()
    interface = options.interface
    mac_address = options.mac_address
    if not interface:
        parser.error("******INTERFACE PODU DA BODY SODA******")
    elif not mac_address:
        parser.error("******MAC-ADDRESS PODU DA BODY SODA*****")
    else:
        return (interface, mac_address)


def get_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    filter_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    mac_filtered_result = filter_result.group(0)
    print("***********************************")
    print("*                                 *")
    print("*  Current " + mac_filtered_result + "      *")
    print("*                                 *")
    print("***********************************")

def process(interface, mac_address):
    subprocess.call(["ifconfig", interface,  "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def compare(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    filter_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    mac_filtered_result = filter_result.group(0)

    if mac_filtered_result == mac_address:
        #print("Mac address changed " + mac_address)
        print("******************************************")
        print("*                                        *")
        print("*  Mac address changed " + mac_address + " *")
        print("*                                        *")
        print("******************************************")
    else:
        print("******************************************")
        print("*                                        *")
        print("*       Mac address not changed          *")
        print("*                                        *")
        print("******************************************")


(interface, mac_address) = get_options()
get_mac(interface)
process(interface, mac_address)
compare(interface)

