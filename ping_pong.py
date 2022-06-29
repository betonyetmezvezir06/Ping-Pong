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

#Raketleri oluşturacağım sınıf
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


game = True
FPS = 60
clock = time.Clock()

yatay_hiz = 3
dikey_hiz = 3


font.init()
yazi_taslagi = font.Font(None,40)
lose1 = yazi_taslagi.render("1. OYUNCU KAYBETTİ!",True,(0,0,0))
lose2 = yazi_taslagi.render("2. OYUNCU KAYBETTİ!",True,(0,0,0))


while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    pencere.fill((200,255,255))
    raket_sag.ciz()
    raket_sol.ciz()
    top.ciz()

    raket_sol.update_l()
    raket_sag.update_r()


    top.rect.x = top.rect.x + yatay_hiz
    top.rect.y = top.rect.y + dikey_hiz


    if top.rect.y > 450 or top.rect.y < 0:
        dikey_hiz = dikey_hiz * (-1)


    if sprite.collide_rect(raket_sol,top) or sprite.collide_rect(raket_sag,top):
        yatay_hiz = yatay_hiz * (-1)


    if top.rect.x < 0:
        pencere.blit(lose1,(200,200))
    if top.rect.x > 600:
        pencere.blit(lose2,(200,200))

    display.update()
    clock.tick(FPS)

