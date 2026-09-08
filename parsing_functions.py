def parse_current_firmware(firmware_json:dict) -> str:
    return firmware_json["current_version"]

def parse_bytes(bytes:int) -> tuple[int, int, int]:
    bytes_kb = bytes / 1024
    bytes_mb = bytes_kb / 1024
    bytes_gb = bytes_mb / 1024
    return bytes_kb, bytes_mb, bytes_gb

def parse_interface_data(interface_json:dict):
    for key, value in interface_json.items():
        if value["description"] == None:
            continue
        elif value["statistics"] == {}:
            continue
        else:
            tx_bytes = value["statistics"]["tx_bytes"]
            rx_bytes = value["statistics"]["rx_bytes"]
            tx_bytes_kb, tx_bytes_mb, tx_bytes_gb = parse_bytes(tx_bytes)
            rx_bytes_kb, rx_bytes_mb, rx_bytes_gb = parse_bytes(rx_bytes)
            print(f"\n{key}: {value['description']}")
            print(f"Transmitted bytes: {value["statistics"]["tx_bytes"]}")
            print(f"Transmitted KB: {tx_bytes_kb:.2f}")
            print(f"Transmitted MB: {tx_bytes_mb:.2f}")
            print(f"Transmitted GB: {tx_bytes_gb:.2f}")

            print(f"Received bytes: {value["statistics"]["rx_bytes"]}")
            print(f"Received KB: {rx_bytes_kb:.2f}")
            print(f"Received MB: {rx_bytes_mb:.2f}")
            print(f"Received GB: {rx_bytes_gb:.2f}")

        if "utilization" not in value["rate_statistics"]:
           print(f"Utilization is 0%") 
        else:
            utilization = value["rate_statistics"]["utilization"]
            print(f"Utilization: {utilization:.2f}%")
    return
