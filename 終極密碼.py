import random

def 終極密碼遊戲():
    print("歡迎來到終極密碼遊戲！")
    
    while True:
        # 輸入終極密碼範圍
        最小值 = int(input("請輸入最小值："))
        最大值 = int(input("請輸入最大值："))
        
        # 隨機選擇一個終極密碼
        正確數字 = random.randint(最小值, 最大值)
        
        猜的次數 = 0
        猜測 = 0
        
        while 猜測 != 正確數字:
            猜測 = int(input(f"請猜一個{最小值}到{最大值}的數字："))
            猜的次數 += 1
            
            if 猜測 < 正確數字:
                print("太小了，再猜一次！")
                最小值 = 猜測 + 1
            elif 猜測 > 正確數字:
                print("太大了，再猜一次！")
                最大值 = 猜測
        
        print(f"恭喜你猜對了！終極密碼是 {正確數字}。")
        
        # 問玩家是否重新開始
        再玩一次 = input("是否要重新開始遊戲？(是/否)：")
        if 再玩一次.lower() != '是':
            print("遊戲結束，謝謝參與！")
            break

# 開始遊戲
終極密碼遊戲()
