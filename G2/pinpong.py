from pygame import *

window = display.set_mode((600, 500))
display.set_caption('pinpong_v1')

window.fill((200, 250, 255))

game = True
finish = False
clock = time.Clock()


win_width = 600
win_height = 500




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


#победа
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(
    'rocket 1 Lose!', True, (180, 0, 0))
lose2 = font1.render(
    'rocket 2 Lose!', True, (180, 0, 0))




#проигрыш
font = font.SysFont(None, 70)
win = font.render(
    'YOU LOSE', True, (255, 215, 0)
)
rocket1 = Player('platform.png', 30, 200, 5, 50, 150)
rocket2 = Player('platform.png', 520, 200, 5, 50 , 150)
bol = GameSprite('sharik.png', 300, 250, 16, 50, 50)
speed_x = 4
speed_y = 4
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((200, 250, 255))
        bol.rect.x += speed_x
        bol.rect.y += speed_y

        rocket1.update1()
        rocket2.update2()
        
        
    #y
        if bol.rect.y > win_height-50 or bol.rect.y < 0:
                speed_y *= - 1
        #x  
        if bol.rect.x > win_height-50 or bol.rect.x < 0:
                speed_x *= -1

        if sprite.collide_rect(rocket1, bol) or sprite.collide_rect(rocket2, bol):
                speed_x *= -1

        if bol.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if bol.rect.x > 550:
            finish = True
            window.blit(lose2, (200, 200))
        rocket1.reset()
        rocket2.reset()
        bol.reset()

    display.update()
    clock.tick(60)
