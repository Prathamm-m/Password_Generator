import speedtest

def convert_speed(bits_per_second):
    return round(bits_per_second / (1024 * 1024), 2)  # Convert to Mbps

def run_speed_test():
    print("Running network speed test...\n")
    st = speedtest.Speedtest()

    print("Finding best server...")
    st.get_best_server()

    print("Testing download speed...")
    download_speed = convert_speed(st.download())

    print("Testing upload speed...")
    upload_speed = convert_speed(st.upload())

    ping = st.results.ping

    print("\n------ Speed Test Results ------")
    print(f"Download Speed : {download_speed} Mbps")
    print(f"Upload Speed   : {upload_speed} Mbps")
    print(f"Ping           : {ping} ms")
    print("--------------------------------")

if __name__ == "__main__":
    run_speed_test()