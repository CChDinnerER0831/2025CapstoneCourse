import serial
import csv
from datetime import datetime
import time  # 用來計時

def log_capacitor_data(PORT, BAUD, duration=10):
    # 建立以開機時間為名的 CSV 檔
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"2025_capstoneProject\data\capacitor_data_{timestamp}.csv"

    ser = serial.Serial(PORT, BAUD, timeout=1)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # 等待 Arduino 開始輸出並擷取標題
        while True:
            line = ser.readline().decode().strip()
            if "Voltage" in line:
                writer.writerow(line.split(","))
                break

        print(f"📂 Logging to {filename}... (Ctrl+C to stop)")

        start_time = time.time()  # 開始計時

        try:
            while True:
                line = ser.readline().decode().strip()

                # 檢查是否超過設定時間
                elapsed_time = time.time() - start_time
                if elapsed_time > duration:
                    print(f"\n🛑 Logging stopped after {duration} seconds.")
                    break  # 超過 10 秒後停止紀錄

                if line:
                    print(line)
                    writer.writerow(line.split(","))
        except KeyboardInterrupt:
            print("\n🛑 Logging stopped.")

if __name__ == '__main__':

    log_capacitor_data(0,0)