import pygame as py
import sys
import traceback
from class_snake import Snake, Enemy, Inc, Hinder1, Hinder2, Hinder3, Hinder4, Hinder5


def inc_move(length, head_position, snake_list):
    if length > 1:
        for vol in range(length - 1):
            mov = [head_position[0] - snake_list[vol + 1].rect.centerx,
                   head_position[1] - snake_list[vol + 1].rect.centery]
            head_position = [snake_list[vol + 1].rect.centerx,
                             snake_list[vol + 1].rect.centery]
            snake_list[vol + 1].move(mov)


Black = (0, 0, 0)


def main():
    py.init()
    bg_size = width, height = 900, 506
    screen = py.display.set_mode(bg_size)
    py.display.set_caption('snake')
    bg_image = py.image.load('images/bg_image.png').convert_alpha()
    again_image = py.image.load('images/again.png').convert_alpha()
    again_rect = again_image.get_rect()
    again_rect.center = width/2, 240
    gameover_image = py.image.load('images/gameover.png').convert_alpha()
    gameover_rect = gameover_image.get_rect()
    gameover_rect.center = width/2, 360

    # 实例化
    head = Snake(bg_size)
    snake_group = py.sprite.Group()
    enemy_group = py.sprite.Group()
    snake_list = []
    # snake_group.add(head)
    snake_list.append(head)
    hinder_list = []
    # 分数显示
    score_font = py.font.Font('font/font.ttf', 30)
    # 移动方向标志
    flag = 0
    # 移动速度标志位
    delay = 0
    # 难度提升
    # Level = py.USEREVENT
    # level_num = 0
    # 果实生成
    tar = Enemy(bg_size)
    while py.sprite.spritecollide(tar, snake_group, False):
        tar = Enemy(bg_size)

    clock = py.time.Clock()
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        # snake颜色控制标志
        snake_index = 0
        # 背景显示
        screen.blit(bg_image, (0, 0))
        if head.active:
            # 控制移动方向
            key_pressed = py.key.get_pressed()
            if key_pressed[py.K_w] or key_pressed[py.K_UP] and flag != 1:
                flag = 0
            if key_pressed[py.K_s] or key_pressed[py.K_DOWN] and flag != 0:
                flag = 1
            if key_pressed[py.K_a] or key_pressed[py.K_LEFT] and flag != 3:
                flag = 2
            if key_pressed[py.K_d] or key_pressed[py.K_RIGHT] and flag != 2:
                flag = 3

            length = len(snake_list)

            head_position = [head.rect.centerx, head.rect.centery]
            if not delay % 3:
                if flag == 0:
                    head.move([0, -16])
                    inc_move(length, head_position, snake_list)
                if flag == 1:
                    head.move([0, 16])
                    inc_move(length, head_position, snake_list)
                if flag == 2:
                    head.move([-16, 0])
                    inc_move(length, head_position, snake_list)
                if flag == 3:
                    head.move([16, 0])
                    inc_move(length, head_position, snake_list)

            # 检测是否吃到
            if py.sprite.collide_rect(head, tar):
                if flag == 0:
                    inc = Inc((head.rect.centerx, head.rect.centery + 16))
                if flag == 1:
                    inc = Inc((head.rect.centerx, head.rect.centery - 16))
                if flag == 2:
                    inc = Inc((head.rect.centerx + 16, head.rect.centery))
                if flag == 3:
                    inc = Inc((head.rect.centerx - 16, head.rect.centery))
                snake_group.add(inc)
                enemy_group.add(inc)
                snake_list.append(inc)
                # 每隔七个增加障碍物
                if not length % 7:
                    hinder = Hinder1()
                    while py.sprite.collide_rect(head, hinder):
                        hinder.reset()
                    enemy_group.add(hinder)
                    hinder_list.append(hinder)
                # 四周边角增加障碍物
                if length == 10:
                    hinder1 = Hinder2()
                    hinder1.rect.left, hinder1.rect.top = 0, 0
                    enemy_group.add(hinder1)
                    hinder2 = Hinder3()
                    hinder2.rect.right, hinder2.rect.top = 900, 0
                    enemy_group.add(hinder2)
                    hinder3 = Hinder4()
                    hinder3.rect.right, hinder3.rect.bottom = 900, 506
                    enemy_group.add(hinder3)
                    hinder4 = Hinder5()
                    hinder4.rect.left, hinder4.rect.bottom = 0, 506
                    enemy_group.add(hinder4)
                    hinder_list.extend([hinder1, hinder2, hinder3, hinder4])

                tar.reset()
                while py.sprite.spritecollide(tar, enemy_group, False, py.sprite.collide_mask):
                    tar.reset()
            # 检测是否死亡
            if py.sprite.spritecollide(head, enemy_group, False, py.sprite.collide_mask):
                head.active = False

            # 障碍物显示
            if hinder_list:
                for each in hinder_list:
                    screen.blit(each.image, each.rect)
            # 分数显示
            score_surface = score_font.render('SCORES : % 04d' % ((length - 1) * 100), True, Black)
            screen.blit(score_surface, (0, 0))
            # 显示蛇
            for vol in range(length):
                screen.blit(
                    snake_list[vol].image[snake_index],
                    snake_list[vol].rect)
                snake_index = (snake_index + 1) % 7
                # print(snake_list[vol].rect,snake_index)
            screen.blit(tar.image, tar.rect)
        # 死亡界面
        else:
            screen.blit(score_surface, (0, 0))
            screen.blit(again_image, again_rect)
            screen.blit(gameover_image, gameover_rect)
            with open('record.txt', 'r') as f:
                last_score = f.read()
            if int(last_score) < ((length-1) * 100):
                last_score = (length - 1) * 100
                with open('record.txt', 'w') as f:
                    f.write(str(last_score))
            top_font = py.font.Font('font/font.ttf', 50)
            top_score = top_font.render('top : %03d' % int(last_score), True, Black)
            screen.blit(top_score, (350, 80))
            if py.mouse.get_pressed()[0]:
                pos = py.mouse.get_pos()
                if 300 < pos[0] < 600 and 220 < pos[1] < 260:
                    main()
                if 300 < pos[0] < 600 and 340 < pos[1] < 380:
                    py.quit()
                    sys.exit()

        delay += 1
        if not delay % 100:
            delay = 0
        py.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except BaseException:
        traceback.print_exc()
