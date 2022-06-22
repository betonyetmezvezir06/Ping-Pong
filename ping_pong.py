from pygame import*

pencere = display.set_mode((600,500))

pencere.fill((200,255,255))

FPS = 60
clock= time.Clock()


game = True

while game:
    for e in event.get():
    
        if e.type ==QUIT:
            game = False

    display.update()
    clock.tick(FPS)