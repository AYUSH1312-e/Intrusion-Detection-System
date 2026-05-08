import sqlite3

def init_db():
    conn = sqlite3.connect('ids_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS alerts 
                 (timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, src_ip TEXT, threat_type TEXT)''')
    conn.commit()
    conn.close()

def save_alert(ip, threat):
    conn = sqlite3.connect('ids_logs.db')
    c = conn.cursor()
    c.execute("INSERT INTO alerts (src_ip, threat_type) VALUES (?, ?)", (ip, threat))
    conn.commit()
    conn.close()