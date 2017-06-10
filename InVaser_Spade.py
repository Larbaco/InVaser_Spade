#!/usr/bin/python

"""
 * 10 de Junho de 2017
 *
 * InVaser_Spade
 *
 * Criado por Thiago O. Cabral
 *
 *
 """
 
 
from objetos import *
from random import randint

viewangle = 1
tippangle = 1
anim_X = 0
anim_Y = 0
speed = 1
speed_proj = 0.5
posx = 0
posy = -30
vet_Projeteis_Nave = []
vet_Projeteis_mob = []
matz_Pos = []
lista_Acertos = []
lista_Particulas = []
lim_projeteis = 100
quant_particulas = 100

vetorFace = [[-0.5,+0.0],[-0.5,-2.0],[+0.5,-2.0],
             [+0.5,+0.0],[+1.5,+0.0],[+1.5,+1.0],
             [+0.5,+1.0],[+0.5,+2.0],[-0.5,+2.0],
             [-0.5,+1.0],[-1.5,+1.0],[-1.5,+0.0]]           #pontos da cruz



def atualiza_particulas():
   global lista_Particulas
   buff = []
   for ponto in lista_Particulas:
      for x in ponto['particulas']:
         particula(ponto['posOrig'][0]+x['pos'][0],ponto['posOrig'][1]+x['pos'][1],x['pos'][2])
         x['pos'][0] += x['dir'][0]
         x['pos'][1] += x['dir'][1]
         x['pos'][2] += x['dir'][2]
         #print x['dir']
      ponto['vida'] -= 1
      if ponto['vida'] > 0:
          buff += [ponto]
   lista_Particulas = buff

def atualiza_pos():
   global anim_X, speed, anim_Y
   flag = False
   if (anim_X == 25) or (anim_X ==  -25):
      speed *= -1
      anim_Y += 1
      flag = True
   anim_X = anim_X + speed
   for x in range(len(matz_Pos)):
      matz_Pos[x][0] += speed
   for x in range(len(lista_Acertos)):
      if flag:
         lista_Acertos[x][1] -= 1
      lista_Acertos[x][0] += speed

def atualiza_pos_projeteis():
   global vet_Projeteis_Nave, vet_Projeteis_mob, speed_proj, lista_Acertos
   buff_remocao_nave = []
   for x in range(len(vet_Projeteis_Nave)):
      aux = vet_Projeteis_Nave[x][1] + speed_proj
      res_Colis = verifica_colisao_mob(aux,vet_Projeteis_Nave[x][0])
      if res_Colis != [] or aux > 50:
         buff_remocao_nave += [[vet_Projeteis_Nave[x][0],aux]]
         if not aux > 50:
            lista_Acertos += [res_Colis]
      vet_Projeteis_Nave[x][1] = aux
   for x in range(len(vet_Projeteis_mob)):
      vet_Projeteis_mob[x][1] -= speed_proj
   #removendo projeteis colididos
   for x in buff_remocao_nave:
      #print 'removendo',x
      vet_Projeteis_Nave.remove(x)


def particula(posy,posx,posz):
   glPushMatrix()
   glColor(randint(0,100)/100.0,randint(0,100)/100.0,randint(0,100)/100.0)
   glTranslatef(posx,posy,posz)
   glutSolidSphere(.3,50,50)
   glPopMatrix()


def verifica_colisao_mob(posy,posx):
   global matz_Pos, lista_Particulas
   for x in matz_Pos:
      if ((posx > (x[0] - ((11*0.3)) )) and (posx < (x[0] + ((11*0.3))))) and ((posy > x[1] - ((6*0.3))) and (posy < x[1] + ((6*0.3)))):
         pontos = []
         for e in range(quant_particulas):
            pontos += [{'dir':[randint(-1000,1000)/1000.0,randint(-1000,1000)/1000.0,randint(-1000,1000)/1000.0],'pos':[0,0,0]}]
         lista_Particulas += [{'posOrig':[posy,posx],'vida':10,'particulas':pontos}];

         return x
   return []


def mob_atira():
   global vet_Projeteis_mob
   for x in matz_Pos:
      if randint(0,500) == 1:
         vet_Projeteis_mob += [[x[0],x[1]]]

def display():
   global anim_X, posx, posy, matz_Pos, vet_Projeteis_Nave, anim_Y
   '''
   if matz_Pos == []:
      glPushMatrix()
      glColor(1,1,1)
      glScalef(1.5,1.5,1)
      glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24 , 38);
      glPopMatrix()
   '''
   atualiza_pos()
   #mob_atira()
   atualiza_pos_projeteis()
   contador = 0
   matz_Pos = []
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)# Limpa a janela e o depth buffer
   glLoadIdentity()
   gluLookAt(0,5,130,0,0,0,0,1,0)
   glRotatef(viewangle,0,1,0)
   glRotatef(tippangle,1,0,0)
   #glRotatef(-60,1,0,0)
   yAtual = 36
   for locy in range(4):
      yAtual -= 6
      xAtual = -25
      for locx in range(10):                                         # Translada
         posAtual = [xAtual + anim_X , yAtual - anim_Y]
         if posAtual not in lista_Acertos:
            matz_Pos += [posAtual]
         xAtual += 5
   contador = 0
   #print len(matz_Pos)
   for posAtual in matz_Pos:
      if contador < 20:
         glColor(0,0.8,0)
         alien_A(posAtual[0],posAtual[1],-1)
      else:
         glColor(0,0,0.8)
         alien_B(posAtual[0],posAtual[1],-1)
      contador += 1

   glPushMatrix()
   glTranslatef(posx,posy,0)
   glRotatef(180,0,0,1)
   glColor(0.8,0,0)
   face_nave_Player(vetorFace,-0.5)
   face_nave_Player(vetorFace,0.5)
   glPopMatrix()

   for x in vet_Projeteis_Nave:
      glPushMatrix()
      projetil(x[0],x[1],0)
      glPopMatrix()
   for x in vet_Projeteis_mob:
      glPushMatrix()
      projetil(x[0],x[1],0)
      glPopMatrix()
   atualiza_particulas()
   glutSwapBuffers()

def initialize():
   glMatrixMode(GL_PROJECTION)
   glViewport(0, 0, 640,500)
   gluPerspective(45, 640/500, 1.0, 500.0)
   glMatrixMode(GL_MODELVIEW)
   glEnable(GL_COLOR_MATERIAL )#habilitadas a cor para o material a partir da cor corrente
   glEnable( GL_DEPTH_TEST )#controla as comparacoes de profundidade e atualiza o depth buffer
   glClearColor(0, 0, 0, 0.0)
   glEnable(GL_LIGHTING)
   glEnable(GL_LIGHT0)
   glEnable(GL_LIGHT1)
   glEnable(GL_DEPTH_TEST)
   lightpos = [2.0, 2.0, 1.0, 1.0]
   lightcol = [0.8, 1.0, 0.0, 1.0]
   lightamb = [1.0, 1.0, 1.0, 1.0]
   glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
   glLightfv(GL_LIGHT0, GL_DIFFUSE, lightcol)
   glLightfv(GL_LIGHT1, GL_AMBIENT, lightamb)

def executa():
   glutInit(len(sys.argv),sys.argv)
   glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH)
   glutInitWindowSize(640,500)
   glutCreateWindow('Space Invaders')
   glutDisplayFunc(display)
   glutIdleFunc(display)
   glutSpecialFunc(movimenta)
   glutKeyboardFunc(Keys)
   initialize()
   glutMainLoop()

def Keys(key,x,y):
   global viewangle, tippangle, posx, posy, vet_Projeteis_Nave, lim_projeteis
   if key == 'a': viewangle -= 5
   elif key == 'd': viewangle += 5
   elif key == 'w': tippangle -= 5
   elif key == 's': tippangle += 5
   elif key == ' ':
      if len (vet_Projeteis_Nave) < lim_projeteis:
         vet_Projeteis_Nave += [[posx,posy]]
   elif key == '\033': sys.exit( )
   glutPostRedisplay()

def movimenta(key,x,y):
   global posx, posy
   if key == GLUT_KEY_LEFT: posx -= 1
   elif key == GLUT_KEY_RIGHT: posx += 1
   elif key == GLUT_KEY_UP: posy = posy
   elif key == GLUT_KEY_DOWN: posy = posy
   glutPostRedisplay()

executa()
