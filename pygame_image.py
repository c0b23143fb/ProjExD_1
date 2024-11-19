import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600)) #surface
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #問題1 背景画像surfaceを作成する
    bg_img2 = pg.transform.flip(bg_img, True, False) #フリップ下背景surface
    flykk_img = pg.image.load("fig/3.png") 
    flykk_img = pg.transform.flip(flykk_img, True, False) #左右反転 #(画像surface, 左右を反転させるか、上下を反転させるか)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0]) #screen sarfaceに背景画像surfaceを貼り付ける
        #(背景画像surface, 画面の位置) #問題3
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(flykk_img, [300, 200]) #screen sarfaceにこうかとん画像surfaceを貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200) #FPS

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()