def parse_current_firmware(firmware_json:dict) -> str:
    return firmware_json["current_version"]

def parse_bytes(bytes:int) -> tuple[float, float, float]:
    bytes_kb = round(bytes / 1024, 2)
    bytes_mb = round(bytes_kb / 1024, 2)
    bytes_gb = round(bytes_mb / 1024, 2)
    return bytes_kb, bytes_mb, bytes_gb

def parse_rates(Bytes_per_second:float) -> tuple[float, float, float]:
    bps = round(Bytes_per_second * 8, 2)
    kbps = round(bps / 1024, 2)
    mbps = round (kbps / 1024, 2)
    return bps, kbps, mbps

def parse_interface_data(interface_json:dict) -> list[dict]:
    all_int_stats = [] # list of dicts
    for key, value in interface_json.items():
        stats_dict = {}
        if value["description"] == None:
            continue
        elif value["statistics"] == {}:
            continue
        elif value["rate_statistics"] == {}:
            continue
        else:
            description:str = value["description"]
            tx_bytes:int = value["statistics"]["tx_bytes"]
            rx_bytes:int = value["statistics"]["rx_bytes"]
            tx_bytes_kb, tx_bytes_mb, tx_bytes_gb = parse_bytes(tx_bytes)
            rx_bytes_kb, rx_bytes_mb, rx_bytes_gb = parse_bytes(rx_bytes)

            total_Bps:float = value["rate_statistics"]["bytes_per_second"]
            rx_Bps:float = value["rate_statistics"]["rx_bytes_per_second"]
            tx_Bps:float = value["rate_statistics"]["tx_bytes_per_second"]
            total_bps, total_kbps, total_mbps = parse_rates(total_Bps)
            rx_bps, rx_kbps, rx_mbps = parse_rates(rx_Bps)
            tx_bps, tx_kbps, tx_mbps = parse_rates(tx_Bps)
            print(round(total_Bps))
            print(total_kbps)
            print(total_mbps)

            stats_dict["interface"] = key
            stats_dict["description"] = description
            stats_dict["tx_bytes"] = tx_bytes
            stats_dict["tx_bytes_kb"] = tx_bytes_kb
            stats_dict["tx_bytes_mb"] = tx_bytes_mb
            stats_dict["tx_bytes_gb"] = tx_bytes_gb
            stats_dict["rx_bytes"] = rx_bytes
            stats_dict["rx_bytes_kb"] = rx_bytes_kb
            stats_dict["rx_bytes_mb"] = rx_bytes_mb
            stats_dict["rx_bytes_gb"] = rx_bytes_gb

            stats_dict["total_Bps"] = round(total_Bps)
            stats_dict["total_bps"] = total_bps
            stats_dict["total_kbps"] = total_kbps
            stats_dict["total_mbps"] = total_mbps
            stats_dict["rx_bps"] = rx_bps
            stats_dict["rx_kbps"] = rx_kbps
            stats_dict["rx_mbps"] = rx_mbps
            stats_dict["tx_bps"] = tx_bps
            stats_dict["tx_kbps"] = tx_kbps
            stats_dict["tx_mbps"] = tx_mbps

        if "utilization" not in value["rate_statistics"]:
           stats_dict["util_pct"] = 0
        else:
            util_pct:float = value["rate_statistics"]["utilization"]
            stats_dict["util_pct"] = round(util_pct, 2)
        all_int_stats.append(stats_dict)
    return all_int_stats
