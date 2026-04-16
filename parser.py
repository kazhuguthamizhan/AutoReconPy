import xml.etree.ElementTree as ET

def parse_nmap_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    results = {
        "ports": [],
        "os": "Unknown"
    }

    # Extract ports
    for port in root.findall(".//port"):
        port_id = port.get("portid")
        protocol = port.get("protocol")

        state = port.find("state").get("state")
        if state != "open":
            continue

        service = port.find("service")
        service_name = service.get("name") if service is not None else "unknown"
        product = service.get("product") if service is not None else ""
        version = service.get("version") if service is not None else ""

        results["ports"].append({
            "port": port_id,
            "protocol": protocol,
            "service": service_name,
            "product": product,
            "version": version
        })

    # Extract OS (if available)
    osmatch = root.find(".//osmatch")
    if osmatch is not None:
        results["os"] = osmatch.get("name")

    return results
