import time
from log_data import log_capacitor_data
from plot_voltage import plot_capacitor_voltage

def main():
    # 設定 Arduino 的端口和波特率
    PORT = 'COM9'
    BAUD = 9600
    
    # 根據需要調用功能
    print("選擇操作：")
    print("1. 繪製電壓圖")
    print("2. 從 Arduino 讀取數據並記錄")
    choice = input("請輸入選項（1/2）：")

    if choice == '1':
        filename = input("請輸入 CSV 檔案名稱：")
        plot_capacitor_voltage(filename)
    elif choice == '2':
        # 在這裡設置紀錄時間為 10 秒
        duration = 600  # 設置停止紀錄的時間為 10 秒
        confirmation = input(f"你確定要從 Arduino 開始記錄數據嗎？（按 'y' 確定，按其他鍵取消）：")
        
        if confirmation.lower() == 'y':
            log_capacitor_data(PORT, BAUD, duration)  # 調用 log_capacitor_data，並設置停止時間
        else:
            print("操作已取消。")
    else:
        print("無效選擇。請選擇 1 或 2。")

if __name__ == '__main__':
    main()
