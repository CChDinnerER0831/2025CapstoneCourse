import csv
import matplotlib.pyplot as plt

def plot_capacitor_voltage(filename):
    time_list_ms = []
    voltage_list = []

    # 用 'utf-8-sig' 編碼來讀檔
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # 跳過標題行
        for row in reader:
            # 檢查是否為有效數據行
            try:
                time_ms = int(row[0])  # 嘗試將第一欄轉為整數
                voltage = float(row[1])  # 嘗試將第二欄轉為浮點數
                time_list_ms.append(time_ms)
                voltage_list.append(voltage)
            except ValueError:
                # 如果有錯誤（例如非數字字串），就跳過這行
                continue

    # ➡️ 將毫秒轉換為秒
    time_list_s = [t / 1000.0 for t in time_list_ms]

    # 繪圖
    plt.figure(figsize=(10, 5))
    plt.plot(time_list_s, voltage_list, label='Voltage', color='blue')
    plt.xlabel('Time (s)')  # 改為秒
    plt.ylabel('Voltage (V)')
    plt.title('Capacitor Voltage Over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    plot_capacitor_voltage('')