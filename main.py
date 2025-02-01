import pyautogui
import time
import os
import sys

# メニュー表示
print("--------------------")
print("実行する自動化プログラムを選択してください:")
print("1. 座標ターゲット")
print("2. 自動ハート受け取り")
print("3. 自動ハートプレゼント")
print("※ q を押すとプログラムを終了します。")
print("--------------------")

while True:
    # ユーザー選択
    choice = input("選択肢を入力してください（1/2/3 または 'q' で終了）: ").strip()

    # 終了条件
    if choice.lower() == "q":
        print("プログラムを終了します。")
        sys.exit()

    # 各選択肢による分岐
    if choice == "1":
        print("座標ターゲットを実行します。")

        # 座標取得プログラム
        print("マウスを目的の位置に移動してください。Ctrl+Cで終了します。")
        time.sleep(2)  # 準備のための待機

        try:
            previous_position = None  # 前回の座標を記憶
            while True:
                x, y = pyautogui.position()
                current_position = (x, y)

                # 座標が変化した場合のみ表示を更新
                if current_position != previous_position:
                    os.system('clear')  # 画面をリフレッシュ（Linux/Macの場合、Windowsでは 'cls' に変更）
                    print(f"現在の座標: ({x}, {y})")
                    previous_position = current_position

                time.sleep(0.2)  # 更新間隔を調整
        except KeyboardInterrupt:
            print("\n終了しました。")
        break

    elif choice == "2":
        # 自動処理の回数を入力
        try:
            repeat_count = int(input("自動処理の回数を入力してください: ").strip())
            if repeat_count <= 0:
                print("回数は1以上の整数で入力してください。")
                continue
        except ValueError:
            print("無効な入力です。整数を入力してください。")
            continue

        print("自動ハート受け取りを実行します。")

        # 各クリック操作と待機時間を設定
        click_sequence = [
            {"position": (320, 420), "delay": 1},  # 最初の座標を更新
            {"position": (300, 610), "delay": 1}  # 次の座標を更新
        ]

        # クリック操作を指定回数繰り返す
        for _ in range(repeat_count):
            for step in click_sequence:
                position = step["position"]
                delay = step["delay"]
                pyautogui.click(*position)
                time.sleep(delay)
                pyautogui.click(*position)

        print("クリック操作が完了しました。")
        break

    elif choice == "3":
        print("自動ハートプレゼントは現在未実装です。")
        break

    else:
        print("無効な選択肢です。もう一度入力してください。")