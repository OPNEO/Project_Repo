import stomp
import json
from datetime import datetime

class TrustListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print(f"❌ ERROR: {frame.body}")

    def on_connected(self, headers):  # still takes only 'headers'
        print("✅ Connected to Network Rail TRUST feed.")

    def on_message(self, frame):  # ✅ FIX: only one argument
        print("\n📨 Message Received:")
        try:
            data = json.loads(frame.body)
            for msg in data:
                msg_type = msg["header"].get("msg_type")
                print(f"🔹 Type: {msg_type}")
                print(json.dumps(msg, indent=2))
        except Exception as e:
            print(f"❌ Error parsing message: {e}")

conn = stomp.Connection(host_and_ports=[('datafeeds.networkrail.co.uk', 61618)])
conn.set_listener('', TrustListener())

username = 'opdante0321@gmail.com'  # Replace with your NTROD username
password = 'Cmdacq@65'  # Replace with your NTROD password

conn.connect(username, password, wait=True)

# Subscribe to TRAIN_MVT_ALL_TOC topic
conn.subscribe(destination='/topic/TRAIN_MVT_EA_TOC', id=1, ack='auto')

# Keep the script running
print("📡 Listening for train movement messages... Press Ctrl+C to stop.")
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n🛑 Disconnected.")
    conn.disconnect()
