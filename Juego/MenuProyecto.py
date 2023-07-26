import pygame #Importa la biblioteca pygame, que proporciona funcionalidades para crear videojuegos y aplicaciones multimedia.
import pygame_menu #Importa la biblioteca pygame_menu, que proporciona funcionalidades para crear menús en pygame.
from main import Main #Importar el main del juego

def Principal():
    pygame.init() #Inicializa todos los módulos de pygame importados.
    Surface = pygame.display.set_mode((1000, 600)) #Crea una ventana de 1000x600 píxeles.
    pygame.display.set_caption("Martial Mayhem") #Da el nombre a la ventana de

    #cargar y escalar la imagen de fondo del menu
    Fondo_Menu = pygame.image.load('Juego/Assets/Imagenes/Background/Fondo_Menu.jpg')
    Fondo_Menu = pygame.transform.scale(Fondo_Menu,(1000,600))

    #Esta función ejecuta el juego principal llamando a la función Main() importada del archivo main.py.
    def StartGame():
        Main()

    #Esta función muestra un submenú con información sobre el juego, como introducción, mecánicas, personajes, créditos y derechos de autor.
    def InfoGame():
        Submenu = pygame_menu.Menu('Información del juego', 1000, 600,
                                    theme=pygame_menu.themes.THEME_BLUE) #Crea un submenú con el título "Información del juego" y con un tamaño de 600x300 píxeles.
        Submenu.add.button('Introducción', IntrodutionGame) #Crea un botón para ir a la función IntrodutionGame
        Submenu.add.button('Mecánicas', MechanicsGame) #Crea un botón para ir a la función MechanicsGame
        Submenu.add.button('Personajes', PlayersGame) #Crea un botón para ir a la función PlayersGame
        Submenu.add.button('Créditos', CreditsGame) #Crea un botón para ir a la función CreditsGame
        Submenu.add.button('Derechos de autor', LinksGame) #Crea un botón para ir a la función LinksGame
        Submenu.add.button('Volver al menú principal', Principal) #Crea un botón para ir a la función Menu
        Submenu.mainloop(Surface) #Muestra el submenú

    #Esta función muestra un submenú con la introducción del juego y otra información relacionada.
    def IntrodutionGame():
        Submenu = pygame_menu.Menu('Introducción', 1000, 600,
                                    theme=pygame_menu.themes.THEME_BLUE) #Crea un submenú con el título "Introducción" y con un tamaño de 883x497 píxeles.
        
        #Texto que se mostrará en la pantalla.
        Intro = '''        
            Título: Martial mayhem
            Concepto principal: El juego consiste en dos luchadores peleando entre sí en un escenario, en donde cada uno constará de ciertas habilidades que les servirán para ganar.
            Género: Arcade.
            Propósito: Este juego está creado como parte del proyecto final de la asignatura de computación gráfica para la Universidad Tecnológica de Pereira, y está dirigido principalmente para los estudiantes de la materia y el profesor. Si es posible publicar el juego en github o en alguna plataforma similar lo haremos.
            Jugabilidad: El objetivo del juego se basa en pelear hasta que a alguno de los jugadores no les quede vida y por ende mueran, para lograr esto tendrán ciertas armas y habilidades que son exclusivas del personaje, y no se podrán recoger elementos extra en el juego.
            Estilo visual: El juego tendrá un entorno en 2D en donde los personajes podrán saltar y golpear, y en donde se tendrá de fondo un escenario. Este juego se basa en el estilo visual de juegos como street fighter o king of fighter; en otras palabras juegos para consolas antiguas como los son la game boy o el nintendo 64.
            Plataforma: El juego se realizará en el entorno de python, utilizando la librería gráfica de pygame. Y no se tiene planeado que el juego sea lanzado a ninguna plataforma de juegos actual.'''
            
        Custom_Theme = pygame_menu.themes.THEME_BLUE.copy()  # Copiar el tema existente
        Custom_Theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT  # Alinear el texto a la izquierda

        Submenu._theme = Custom_Theme  # Establecer el tema personalizado
        Submenu.add.label(Intro) #Muestra el texto en la pantalla
        Submenu.add.button('Volver', InfoGame) #Crea un botón para volver al submenú
        Submenu.mainloop(Surface) #Retorna al submenú

    #Esta función muestra un submenú con las mecánicas del juego, incluyendo el tipo de cámara, los controles, la puntuación, los niveles y las habilidades.
    def MechanicsGame():
        Submenu = pygame_menu.Menu('Mecánicas del juego', 1000, 600,
                                    theme=pygame_menu.themes.THEME_BLUE) #Crea un submenú con el título "Mecánicas del juego" y con un tamaño de 883x497 píxeles.
        
        #Texto que se mostrará en la pantalla.
        Mechanics = '''
            Tipo de cámara: El juego utilizará una cámara estática en 2D.
            Controles: 

            Jugador 1:

            Flecha arriba: Saltar
            Flecha derecha: Moverse a la derecha
            Flecha izquierda: Moverse a la izquierda
            Ctrl izquierdo: Ataque 1
            z: ataque 2


            Jugador 2:

            w: Saltar
            a: Moverse a la derecha
            d: Moverse a la izquierda
            Ctrl derecho: Ataque 1
            m: ataque 2

            Puntuación: El juego no tendrá una puntuación, sin embargo constará con una barra de vida, la cual al llegar a 0 determinará el ganador y el perdedor.
            Niveles: Tampoco contará con niveles, el juego tendrá un escenario único, con una única temática.
            Habilidades: Los personajes no tendrán habilidades especiales dentro del juego, estos contarán con armas propias de cada uno de su personaje (ya sea una espada, o algún otro de tipo arma, la cual dependerá del personaje que se escoja).
            '''
            
        Custom_Theme = pygame_menu.themes.THEME_BLUE.copy()  # Copiar el tema existente
        Custom_Theme.font = 'Segoe UI Font'
        Custom_Theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT  # Alinear el texto a la izquierda

        Submenu._theme = Custom_Theme  # Establecer el tema personalizado
        Submenu.add.label(Mechanics) #Muestra el texto en la pantalla
        Submenu.add.button('Volver', InfoGame) #Crea un botón para volver al submenú
        Submenu.mainloop(Surface) #Retorna al submenú

    #Esta función muestra un submenú con información sobre los personajes del juego, incluyendo sus descripciones.
    def PlayersGame():
        Submenu = pygame_menu.Menu('Personajes', 1000, 600,
                                    theme=pygame_menu.themes.THEME_BLUE) #Crea un submenú con el título "Personajes" y con un tamaño de 883x497 píxeles.
        
        #Texto que se mostrará en la pantalla.
        Players = '''
            Azazel: Es un hechicero que porta una varita mágica, parece un anciano que no puede moverse, pero su apariencia te puede engañar. Es alguien muy hábil y con unos poderes mágicos sorprendentes, de los cuales no te voy a hacer spoiler.
            Yakuza: Es un samurai proveniente de Japón, es un muy hábil espadachín, que carga con varias bajas en su haber, sin duda será un contendiente muy difícil de vencer.
            '''
            
        Custom_Theme = pygame_menu.themes.THEME_BLUE.copy()  # Copiar el tema existente
        Custom_Theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT  # Alinear el texto a la izquierda

        Submenu._theme = Custom_Theme  # Establecer el tema personalizado
        Submenu.add.label(Players) #Muestra el texto en la pantalla
        Submenu.add.button('Volver', InfoGame) #Crea un botón para volver al submenú
        Submenu.mainloop(Surface) #Retorna al submenú

    #Esta función muestra un submenú con los créditos del juego, incluyendo los nombres de los creadores y la información de la universidad y el curso.
    def CreditsGame():
        Submenu = pygame_menu.Menu('Créditos', 1000, 600,
                                    theme=pygame_menu.themes.THEME_BLUE) #Crea un submenú con el título "Créditos" y con un tamaño de 883x497 píxeles.
        
        #Texto que se mostrará en la pantalla.
        Credits = '''
            Oscar Julián Cárdenas
            Nicolás Orozco Flórez
        
            Universidad Tecnológica de Pereira
            Computación Gráfica
            2023-1
            '''
        
        Custom_Theme = pygame_menu.themes.THEME_BLUE.copy()  # Copiar el tema existente
        Custom_Theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT  # Alinear el texto a la izquierda
        
        Submenu._theme = Custom_Theme  # Establecer el tema personalizado
        Submenu.add.label(Credits) #Muestra el texto en la pantalla
        Submenu.add.button('Volver', InfoGame) #Crea un botón para volver al submenú
        Submenu.mainloop(Surface) #Retorna al submenú

    #Esta función muestra un submenú con enlaces a los recursos utilizados en el juego, como los escenarios, los personajes y los sonidos.
    def LinksGame():
        Submenu = pygame_menu.Menu('Derechos de autor', 1000, 600,
                                    theme=pygame_menu.themes.THEME_BLUE) #Crea un submenú con el título "Derechos de autor" y con un tamaño de 883x497 píxeles.
        
        #Texto que se mostrará en la pantalla.
        Links = '''
        Escenarios:
            https://opengameart.org/content/backgrounds-3
            https://opengameart.org/content/background-6
            
        Personajes:
            https://luizmelo.itch.io/wizard-pack
            https://luizmelo.itch.io/martial-hero-2
            
        Sonidos:
            https://freesound.org/people/mrrap4food/sounds/493918/
            https://freesound.org/people/Herkules92/sounds/547600/
            https://freesound.org/people/qubodup/sounds/442872/
            '''
        
        Custom_Theme = pygame_menu.themes.THEME_BLUE.copy()  # Copiar el tema existente
        Custom_Theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT  # Alinear el texto a la izquierda
        
        Submenu._theme = Custom_Theme  # Establecer el tema personalizado
        Submenu.add.label(Links) #Muestra el texto en la pantalla
        Submenu.add.button('Volver', InfoGame) #Crea un botón para volver al submenú
        Submenu.mainloop(Surface) #Retorna al submenú

    #Esta función dibuja el fondo del menú en la ventana de visualización utilizando la imagen cargada y escalada anteriormente.
    def Draw_Background():
        Surface.blit(Fondo_Menu, (0, 0)) #Muestra el fondo personalizado

    #Creación del menú principal
    Menu = pygame_menu.Menu('Bienvenido', 1000, 600,
                            theme=pygame_menu.themes.THEME_BLUE) #Crea un menú con el título "Bienvenido" y con un tamaño de 600x300 píxeles.

    #Agregar elementos al menú principal
    Menu.add.button('Fight', StartGame) #Crea un botón para iniciar el juego
    Menu.add.button('A cerca de', InfoGame) #Crea un botón para ir al submenú de "A cerca de"
    Menu.add.button('Quit', pygame_menu.events.EXIT) #Crea un botón para salir del juego

    #Ciclo para navegar por las opciones hasta que el usuario salga de la ventana
    Running = True
    while Running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                Running = False

        Surface.fill((0, 0, 0))
        Menu.update(events)
        Menu.draw(Surface)
        Draw_Background()
        pygame.display.flip()

    pygame.quit()

Principal()