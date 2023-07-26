import pygame
from pygame import mixer
from fighter import Fighter

def Main():
    mixer.init()
    pygame.init()

    # Dimensiones de pantalla
    Ancho_Pantalla = 1000
    Alto_Pantalla = 600
    # Crea la pantalla y se le da nombre 
    Pantalla = pygame.display.set_mode((Ancho_Pantalla, Alto_Pantalla))
    pygame.display.set_caption("Martial Mayhem")

    clock = pygame.time.Clock()
    FPS = 60

    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    Cuenta_Inicial = 3
    Cuenta_Final = pygame.time.get_ticks()
    Score = [0, 0]  
    Round_Over = False
    ROUND_OVER_COOLDOWN = 2000

    # Crea las variables de los personajes 
    MARTIAL_HERO_SIZE = 200
    MARTIAL_HERO_SCALE = 4
    MARTIAL_HERO_OFFSET = [72, 60]
    MARTIAL_HERO_DATA = [MARTIAL_HERO_SIZE, MARTIAL_HERO_SCALE, MARTIAL_HERO_OFFSET]
    EVIL_WIZARD_SIZE = 250
    EVIL_WIZARD_SCALE = 4
    EVIL_WIZARD_OFFSET = [112, 100]
    EVIL_WIZARD_SIZE = [EVIL_WIZARD_SIZE, EVIL_WIZARD_SCALE, EVIL_WIZARD_OFFSET]

    # Carga de sonidos y música
    pygame.mixer.music.load('Juego/Assets/Audio/music.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)
    Sword = pygame.mixer.Sound('Juego/Assets/Audio/sword.wav')
    Sword.set_volume(0.5)
    Magic = pygame.mixer.Sound('Juego/Assets/Audio/magic.wav')
    Magic.set_volume(0.75)

    # Carga de imágenes
    Background = pygame.image.load('Juego/Assets/Imagenes/Background/Background.jpg').convert_alpha()

    # Carga sprites
    Martial_Hero_Sheet = pygame.image.load(
        'Juego/Assets/Imagenes/Martial Hero/Sprites/Fondo/Martial_Hero_2_final.png'
    ).convert_alpha()
    Evil_Wizard_Sheet = pygame.image.load(
        'Juego/Assets/Imagenes/Wizard/evil_wizard.png'
    ).convert_alpha()

    # Carga imagen de victoria
    Victory = pygame.image.load('Juego/Assets/Imagenes/victory.png').convert_alpha()

    # Toma los fotogramas de la imagen del personajes 
    MARTIAL_HERO_STEPS = [4, 8, 2, 4, 4, 3, 7]
    EVIL_WIZARD_STEPS = [6, 8, 2, 8, 8, 4, 7]

    # Fuentes de texto
    Count_Font = pygame.font.Font('Juego/Assets/founts/turok.ttf', 80)
    Score_Font = pygame.font.Font('Juego/Assets/founts/turok.ttf', 30)

    # Escribe el texto en pantalla con la fuente anteriormente definida
    def Draw_Text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        Pantalla.blit(img, (x, y))

    # Dibuja el background del juego
    def Draw_BG():
        scaled_bg = pygame.transform.scale(Background, (Ancho_Pantalla, Alto_Pantalla))
        Pantalla.blit(scaled_bg, (0, 0))

    # Dibuja la barra de vida de los personajes 
    def Draw_Healt_Bar(Health, x, y):
        ratio = Health / 100
        pygame.draw.rect(Pantalla, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(Pantalla, RED, (x, y, 400, 30))
        pygame.draw.rect(Pantalla, YELLOW, (x, y, 400 * ratio, 30))

    # Crea la estancia de los jugadores con la clase Figther
    Player_1 = Fighter(
        1, 200, 310, False, MARTIAL_HERO_DATA, Martial_Hero_Sheet, MARTIAL_HERO_STEPS, Sword
    )
    Player_2 = Fighter(
        2, 700, 310, True, EVIL_WIZARD_SIZE, Evil_Wizard_Sheet, EVIL_WIZARD_STEPS, Magic
    )

    # Se dibuja todo el juego en la ventana
    run = True
    while run:
        clock.tick(FPS)
        # Dibuja el background cuando inicia el juego 
        Draw_BG()
        #Dibuja la barra de vida cuando inicia el juego
        Draw_Healt_Bar(Player_1.Health, 20, 20)
        Draw_Healt_Bar(Player_2.Health, 580, 20)
        Draw_Text("P1: " + str(Score[0]), Score_Font, RED, 20, 60)
        Draw_Text("P2: " + str(Score[1]), Score_Font, RED, 580, 60)
        # Permite a los personajes moverse cuando la cuenta inicial términa
        if Cuenta_Inicial <= 0:
            Player_1.move(Ancho_Pantalla, Alto_Pantalla, Pantalla, Player_2, Round_Over)
            Player_2.move(Ancho_Pantalla, Alto_Pantalla, Pantalla, Player_1, Round_Over)
        else:
            # Dibuja la cuenta inicial
            Draw_Text(
                str(Cuenta_Inicial), Count_Font, RED, Ancho_Pantalla / 2, Alto_Pantalla / 3
            )
            if (pygame.time.get_ticks() - Cuenta_Final) >= 1000:
                Cuenta_Inicial -= 1
                Cuenta_Final = pygame.time.get_ticks()

        Player_1.Update()
        Player_2.Update()

        # Dibuja los jugadores en la pantalla
        Player_1.Draw(Pantalla)
        Player_2.Draw(Pantalla)
        # Aumenta el Score conforme los jugadores sumen victorias
        if Round_Over == False:
            if Player_1.Alive == False:
                Score[1] += 1
                Round_Over = True
                round_over_time = pygame.time.get_ticks()
            elif Player_2.Alive == False:
                Score[0] += 1
                Round_Over = True
                round_over_time = pygame.time.get_ticks()
            if Score [0] == 3 or Score [1] == 3:
                Pantalla.blit(Victory,(360, 150))
                # El primero en ganar 3 rondas gana el juego
                if Score[0] == 3:
                    Draw_Text('El ganador es Yakuza', Score_Font, RED, Ancho_Pantalla/2 - 100, Alto_Pantalla/2)
                elif Score[1] == 3:
                    Draw_Text('El ganador es Azazel', Score_Font, RED, Ancho_Pantalla/2 - 100, Alto_Pantalla/2)
                pygame.display.update()
                pygame.time.delay(5000)
                run = False
        else:
            Pantalla.blit(Victory, (360, 150))
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                Round_Over = False
                Cuenta_Inicial = 3
                Player_1 = Fighter(
                    1,
                    200,
                    310,
                    False,
                    MARTIAL_HERO_DATA,
                    Martial_Hero_Sheet,
                    MARTIAL_HERO_STEPS,
                    Sword,
                )
                Player_2 = Fighter(
                    2,
                    700,
                    310,
                    True,
                    EVIL_WIZARD_SIZE,
                    Evil_Wizard_Sheet,
                    EVIL_WIZARD_STEPS,
                    Magic,
                )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.mixer.music.stop()
