from pygame import*

class Karakter(sprite.Sprite):
    def __init__(self, krk_image, krk_x, krk_y, krk_hiz, genislik, yukseklik):
        super().__init__()
        self.image = transform.scale(image.load(krk_image),(genislik,yukseklik))
        self.hiz = krk_hiz

        self.rect = self.image.get_rect()
        self.rect.x = krk_x
        self.rect.y = krk_y

    def ciz(self):
        pencere.blit(self.image,(self.rect.x,self.rect.y))

class Oyuncu(Karakter):
    def update_r(self):
        basilan_tuslar = key.get_pressed()
        if basilan_tuslar[K_UP] and self.rect.y >5:
            self.rect.y -= self.hiz
        if basilan_tuslar[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.hiz
    def update_l(self):
        basilan_tuslar = key.get_pressed()
        if basilan_tuslar[K_w] and self.rect.y >5:
            self.rect.y -= self.hiz
        if basilan_tuslar[K_s] and self.rect.y < 420:
            self.rect.y += self.hiz

raket_sol = Oyuncu("racket.png",30,200,4,50,150)
raket_sag = Oyuncu("racket.png",520,200,4,50,150)

top = Karakter("tenis_ball.png",200,200,4,50,50)
pencere = display.set_mode((600,500))

pencere.fill((200,255,255))

FPS = 60
clock= time.Clock()


game = True

while game:
    for e in event.get():
    
        if e.type ==QUIT:
            game = False

    raket_sag.ciz()
    raket_sol.ciz()
    top.ciz()

    raket_sag.update_l()
    raket_sag.update_r()

    display.update()
    clock.tick(FPS)
