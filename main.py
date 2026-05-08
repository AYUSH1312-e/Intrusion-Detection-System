import multiprocessing
import sniffer
import database
from app import app

def start_dashboard():
    app.run(port=5000, debug=False, use_reloader=False)

if __name__ == "__main__":
    # 1. Initialize Database
    database.init_db()

    # 2. Start the API/Dashboard in a separate process
    api_process = multiprocessing.Process(target=start_dashboard)
    api_process.start()

    # 3. Start Sniffing in the main process
    try:
        sniffer.start_sniffing()
    except KeyboardInterrupt:
        print("Shutting down...")
        api_process.terminate()
        api_process.join()