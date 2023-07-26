import pygame


class Fighter:
    def __init__(self, Player, x, y, Flip, Data, Sprites, Animation_Steps, Sonido):
        # Constructor de la clase Fighter
        self.Player = Player
        self.Size = Data[0]
        self.Escala_Imagen = Data[1]
        self.Offset = Data[2]
        self.Flip = Flip
        self.Lista_Animacion = self.Load_Images(Sprites, Animation_Steps)
        self.Action = 0  # 0:idle #1:run #2:Jump #3:ataque1 #4:ataque2 #5:Hit #6:death
        self.Frame_Index = 0
        self.Imagen = self.Lista_Animacion[self.Action][self.Frame_Index]
        self.Update_Time = pygame.time.get_ticks()
        self.Back_Rect = pygame.Rect((x, y, 80, 180))
        self.Vel_y = 0
        self.Run = False
        self.Jump = False
        self.Attaking = False
        self.Type_Attack = 0
        self.Attack_Cooldown = 0
        self.Sonido_Attack = Sonido
        self.Hit = False
        self.Health = 100
        self.Alive = True

    def Load_Images(self, Sprites, Animation_Steps):
        # Carga las imágenes para las animaciones del personaje
        Lista_Animacion = []
        for y, Animation in enumerate(Animation_Steps):
            Img_List = []
            for x in range(Animation):
                Temp_Img = Sprites.subsurface(
                    x * self.Size, y * self.Size, self.Size, self.Size
                )
                Img_List.append(
                    pygame.transform.scale(
                        Temp_Img,
                        (self.Size * self.Escala_Imagen, self.Size * self.Escala_Imagen),
                    )
                )
            Lista_Animacion.append(Img_List)
        return Lista_Animacion

    def move(self, Ancho_Pantalla, Alto_Pantalla, Superficie, Target, Round_Over):
        # Actualiza la posición del personaje en función de las teclas presionadas
        VEL = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.Run = False
        self.Type_Attack = 0

        key = pygame.key.get_pressed()

        if self.Attaking == False and self.Alive == True and Round_Over == False:
            if self.Player == 1:
                if key[pygame.K_a]:
                    dx = -VEL
                    self.Run = True
                if key[pygame.K_d]:
                    dx = VEL
                    self.Run = True
                if key[pygame.K_w] and self.Jump == False:
                    self.Vel_y = -30
                    self.Jump = True
                if key[pygame.K_RCTRL] or key[pygame.K_m]:
                    self.Attack(Target)
                    if key[pygame.K_RCTRL]:
                        self.Type_Attack = 1
                    if key[pygame.K_m]:
                        self.Type_Attack = 2

            if self.Player == 2:
                if key[pygame.K_LEFT]:
                    dx = -VEL
                    self.Run = True
                if key[pygame.K_RIGHT]:
                    dx = VEL
                    self.Run = True
                if key[pygame.K_UP] and self.Jump == False:
                    self.Vel_y = -30
                    self.Jump = True
                if key[pygame.K_LCTRL] or key[pygame.K_z]:
                    self.Attack(Target)
                    if key[pygame.K_LCTRL]:
                        self.Type_Attack = 1
                    if key[pygame.K_z]:
                        self.Type_Attack = 2

        self.Vel_y += GRAVITY
        dy += self.Vel_y

        if self.Back_Rect.left + dx < 0:
            dx = -self.Back_Rect.left
        if self.Back_Rect.right + dx > Ancho_Pantalla:
            dx = Ancho_Pantalla - self.Back_Rect.right
        if self.Back_Rect.bottom + dy > Alto_Pantalla - 110:
            self.Vel_y = 0
            self.Jump = False
            dy = Alto_Pantalla - 110 - self.Back_Rect.bottom

        if Target.Back_Rect.centerx > self.Back_Rect.centerx:
            self.Flip = False
        else:
            self.Flip = True

        if self.Attack_Cooldown > 0:
            self.Attack_Cooldown -= 1

        self.Back_Rect.x += dx
        self.Back_Rect.y += dy

    def Update(self):
        # Actualiza la animación del personaje
        if self.Health <= 0:
            self.Health = 0
            self.Alive = False
            self.Update_Action(6)  # 6:death
        elif self.Hit == True:
            self.Update_Action(5)  # 5:Hit
        elif self.Attaking == True:
            if self.Type_Attack == 1:
                self.Update_Action(3)  # 3:attack1
            elif self.Type_Attack == 2:
                self.Update_Action(4)  # 4:attack2
        elif self.Jump == True:
            self.Update_Action(2)  # 2:Jump
        elif self.Run == True:
            self.Update_Action(1)  # 1:run
        else:
            self.Update_Action(0)  # 0:idle

        Animation_Cooldown = 50
        self.Imagen = self.Lista_Animacion[self.Action][self.Frame_Index]
        if pygame.time.get_ticks() - self.Update_Time > Animation_Cooldown:
            self.Frame_Index += 1
            self.Update_Time = pygame.time.get_ticks()
        if self.Frame_Index >= len(self.Lista_Animacion[self.Action]):
            if self.Alive == False:
                self.Frame_Index = len(self.Lista_Animacion[self.Action]) - 1
            else:
                self.Frame_Index = 0
                if self.Action == 3 or self.Action == 4:
                    self.Attaking = False
                    self.Attack_Cooldown = 20
                if self.Action == 5:
                    self.Hit = False
                    self.Attaking = False
                    self.Attack_Cooldown = 20

    def Attack(self, Target):
        # Realiza un ataque al objetivo si el cooldown de ataque está en 0
        if self.Attack_Cooldown == 0:
            self.Attaking = True
            self.Sonido_Attack.play()
            attacking_rect = pygame.Rect(
                self.Back_Rect.centerx - (4 * self.Back_Rect.width * self.Flip),
                self.Back_Rect.y,
                2 * self.Back_Rect.width,
                self.Back_Rect.height,
            )
            if attacking_rect.colliderect(Target.Back_Rect):
                Target.Health -= 10
                Target.Hit = True

    def Update_Action(self, New_Action):
        # Actualiza la acción del personaje
        if New_Action != self.Action:
            self.Action = New_Action
            self.Frame_Index = 0
            self.Update_Time = pygame.time.get_ticks()

    def Draw(self, Superficie):
        # Dibuja al personaje en la superficie
        Img = pygame.transform.flip(self.Imagen, self.Flip, False)
        Superficie.blit(
            Img,
            (
                self.Back_Rect.x - (self.Offset[0] * self.Escala_Imagen),
                self.Back_Rect.y - (self.Offset[1] * self.Escala_Imagen),
            ),
        )
