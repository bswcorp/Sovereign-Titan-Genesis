import time
def send_tembako_alert(amount, destination):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_msg = f"🚀 [TEMBAKO ALERT] | {timestamp} | AMUNISI: {amount} | TARGET: {destination}"
    with open('../TEMBAKO_HISTORY.md', 'a') as f:
        f.write(f"| {timestamp} | {amount} | {destination} | ✅ |\n")
    print("\n" + "📡"*15 + "\n" + log_msg + "\n" + "📡"*15)
