import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.player = "X"
        self.buttons = {}
        self.init_gui()
        
    def init_gui(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.window, text=" ", font=("Helvetica", 20), height=2, width=4, 
                        command=lambda row=i, col=j: self.next_turn(self.buttons[(row, col)]))
                btn.grid(row=i, column=j)
                self.buttons[(i,j)] = btn
        
        self.info = tk.Label(text="玩家X先手", font=("Helvetica", 12)) 
        self.info.grid(row=3, column=0, columnspan=3)
        
    def next_turn(self, btn):
        if btn["text"] == " ":
            btn["text"] = self.player
            if self.player == "X":
                self.player = "O" 
            else:
                self.player = "X"
                
            self.info["text"] = "輪到玩家{}".format(self.player)  
            
            if self.check_win():
                return
        
        elif all([btn["text"] != " " for btn in self.buttons.values()]): 
            self.info["text"] = "平手"
            self.disable_buttons() 
        
        self.check_draw()
            
    def check_win(self):
        # winning combinations
        combos = [[(0,0), (0,1), (0,2)], 
                  [(1,0), (1,1), (1,2)], 
                  [(2,0), (2,1), (2,2)], 
    
                  [(0,0), (1,0), (2,0)], 
                  [(0,1), (1,1), (2,1)],
                  [(0,2), (1,2), (2,2)],
    
                  [(0,0), (1,1), (2,2)],
                  [(2,0), (1,1), (0,2)]]
        
        for combo in combos:
            texts = [self.buttons[pos]["text"] for pos in combo]
            if texts.count(texts[0]) == 3 and texts[0] != " ":
                self.info["text"] = "玩家{}獲勝!".format(self.player)
                self.disable_buttons()
                return True
            
        return False
    
    def check_draw(self):
        if all([btn["text"] != " " for btn in self.buttons.values()]):
            self.info["text"] = "平手"  
            self.disable_buttons()   
            
    def disable_buttons(self):
        for btn in self.buttons.values():
            btn["state"] = "disabled"
            
if __name__ == "__main__":
    game = TicTacToe()  
    game.window.mainloop()
