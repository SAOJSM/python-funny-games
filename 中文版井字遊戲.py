def next_turn(self, btn):
    if btn["text"] == " ":
        btn["text"] = self.player
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"
        self.info["text"] = "輪到玩家{}".format(self.player)
        self.check_win()
    else:
        pass # 按鈕已被佔用,不處理

def check_win(self):
    # 檢查所有可能的勝利條件
    for a, b, c in [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                   [0, 3, 6], [1, 4, 7], [2, 5, 8],
                   [0, 4, 8], [2, 4, 6]]:
        if self.buttons[a]["text"] == self.buttons[b]["text"] == self.buttons[c]["text"] != " ":
            self.disable_all_buttons()
            self.info["text"] = "玩家{}獲勝!".format(self.player)
            return True
    if all([btn["text"] != " " for btn in self.buttons]): 
        # 平局判定
        self.info["text"] = "平手!"
        return "Draw"
    return False

def disable_all_buttons(self):
    for btn in self.buttons:
        btn["state"] = "disabled"
