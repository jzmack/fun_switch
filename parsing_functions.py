import time
import humanize

def parse_system_uptime(boot_time:int) -> str:
    # all times are in seconds
    current_time = int(time.time())
    uptime = current_time - boot_time
    return humanize.precisedelta(uptime)

def parse_system_data(system_data_json:dict) -> dict:
    system_data = system_data_json.copy()
    boot_time = system_data_json.get("boot_time", None)
    uptime = parse_system_uptime(boot_time)
    system_data["uptime"] = uptime
    return system_data

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

        description = value.get("description")
        if not description:
            print(f"no description found for {key}")
            continue

        statistics:dict = value.get("statistics")
        if not statistics:
            print(f"no statistics found for {key}-{value["description"]} ")
            continue

        rate_statistics:dict = value.get("rate_statistics")
        if not rate_statistics:
            print(f"rate statistics not in {key}.")
            continue

        tx_bytes:int = statistics.get("tx_bytes", 0)
        rx_bytes:int = statistics.get("rx_bytes", 0)
        tx_bytes_kb, tx_bytes_mb, tx_bytes_gb = parse_bytes(tx_bytes)
        rx_bytes_kb, rx_bytes_mb, rx_bytes_gb = parse_bytes(rx_bytes)

        total_Bps: float = rate_statistics.get("bytes_per_second", 0.0)
        rx_Bps:float = rate_statistics.get("rx_bytes_per_second", 0.0)
        tx_Bps:float = rate_statistics.get("tx_bytes_per_second", 0.0)
        total_bps, total_kbps, total_mbps = parse_rates(total_Bps)
        rx_bps, rx_kbps, rx_mbps = parse_rates(rx_Bps)
        tx_bps, tx_kbps, tx_mbps = parse_rates(tx_Bps)

        util_pct:float = value.get("utilization", 0.0)

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
        stats_dict["util_pct"] = util_pct

        all_int_stats.append(stats_dict)
    return all_int_stats
