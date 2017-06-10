
"""
 * 10 de Junho de 2017
 *
 * InVaser_Spade
 *
 * Criado por Thiago O. Cabral
 *
 *
 """
  
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objetos import *

def face_nave_Player(vetXY,z):
   # Gera a face da nave
   glBegin(GL_TRIANGLES)
   vetXY = [vetXY[-1]]+vetXY[:-1]
   for n in range(len(vetXY)): glVertex3f(vetXY[n][0],vetXY[n][1],z)
   glVertex3f(vetXY[0][0],vetXY[0][1],z)
   glEnd()

def face_Cruz(vetXY,z):
   # Gera a face da cruz
   parte = 0
   for n in range(4):
      glBegin(GL_QUADS)
      vet_Normal = calcula_Normal(vetXY[parte]+[z],vetXY[parte+1]+[z],vetXY[parte+2]+[z])
      glNormal3f(vet_Normal[0],vet_Normal[1],vet_Normal[2])
      for x in range(4): glVertex3f(vetXY[0][0],vetXY[0][1],z) if x+parte == 12 else glVertex3f(vetXY[x+parte][0],vetXY[x+parte][1],z)
      parte += 3
      glEnd()
      glBegin(GL_QUADS)
      p =[]
      for x in range(4): lixo,p = glVertex3f(vetXY[x*3][0],vetXY[x*3][1],z), p + [x*3]
      vet_Normal = calcula_Normal(vetXY[p[0]]+[z],vetXY[p[1]]+[z],vetXY[p[2]]+[z])
      glNormal3f(vet_Normal[0],vet_Normal[1],vet_Normal[2])
      glEnd()

def liga_Faces(vetorFaceA,vetorFaceB,zA,zB):
   # Liga duas faces de dois objetos

   for n in range(len(vetorFaceA)-1):
      glBegin(GL_QUADS)
      if n == 12: n = 0
      glVertex3f(vetorFaceA[n][0],vetorFaceA[n][1],zA)
      glVertex3f(vetorFaceB[n][0],vetorFaceB[n][1],zB)
      glVertex3f(vetorFaceB[n+1][0],vetorFaceB[n+1][1],zB)
      glVertex3f(vetorFaceA[n+1][0],vetorFaceA[n+1][1],zA)
      glEnd()

def calcula_Normal(p1,p2,p3):
   #
   a,b,n = [0]*3,[0]*3,[0]*3
   for x in range(3): a[x],b[x] = p2[x] - p1[x],p3[x] - p1[x]
   for x in range(3): n[x] = (a[(x+1)%3] * b[(x+2)%3]) - (a[(x+2)%3] * b[(x+1)%3])
   l = (n[0] * n[0] + n[1] * n[1] + n[2] * n[2])**(1/2)
   for x in range(3): n[x] /= l
   return n

def cruz(vetorFace):
   #
   face_Cruz(vetorFace,-0.5)
   face_Cruz(vetorFace,0.5)
   liga_Faces(vetorFace,vetorFace,-0.5,0.5)

def projetil(x,y,z):
   #
   glBegin(GL_QUADS)
   glVertex3f(x-0.2,y-1.5,z)
   glVertex3f(x+0.2,y-1.5,z)
   glVertex3f(x+0.2,y+1.5,z)
   glVertex3f(x-0.2,y+1.5,z)
   glEnd()

def face_alien_A(z):
   '''

      Gera a face do alien A

   '''
   normal = []
   glPushMatrix()
   # Quadrante 1
   glBegin(GL_QUADS)
   normal = calcula_Normal([2.5,-2,z],[2.5,0,z],[-2.5,0,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-2.5,0,z)
   glVertex3f(2.5,0,z)
   glVertex3f(2.5,-2,z)
   glVertex3f(-2.5,-2,z)
   glEnd()

   # Quadrante 2
   glBegin(GL_QUADS)
   #normal = calcula_Normal([1.5,0,z],[1.5,2,z],[-1.5,2,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-1.5,2,z)
   glVertex3f(1.5,2,z)
   glVertex3f(1.5,0,z)
   glVertex3f(-1.5,0,z)
   glEnd()

   # Quadrante 3
   glBegin(GL_QUADS)
   #normal = calcula_Normal([-3.5,2,z],[-3.5,-3,z],[-2.5,-3,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-2.5,-3,z)
   glVertex3f(-3.5,-3,z)
   glVertex3f(-3.5,2,z)
   glVertex3f(-2.5,2,z)
   glEnd()

   # Quadrante 4
   glBegin(GL_QUADS)
   #normal = calcula_Normal([2.5,-3,z],[3.5,-3,z],[3.5,2,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(2.5,-3,z)
   glVertex3f(3.5,-3,z)
   glVertex3f(3.5,2,z)
   glVertex3f(2.5,2,z)
   glEnd()

   # Quadrante 5
   glBegin(GL_QUADS)
   #normal = calcula_Normal([-2.5,-4,z],[-0.5,-4,z],[-0.5,-3,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-2.5,-4,z)
   glVertex3f(-0.5,-4,z)
   glVertex3f(-0.5,-3,z)
   glVertex3f(-2.5,-3,z)
   glEnd()

   # Quadrante 6
   glBegin(GL_QUADS)
   #normal = calcula_Normal([0.5,-3,z],[0.5,-4,z],[2.5,-4,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(2.5,-4,z)
   glVertex3f(0.5,-4,z)
   glVertex3f(0.5,-3,z)
   glVertex3f(2.5,-3,z)
   glEnd()

   # Quadrante 7
   glBegin(GL_QUADS)
   #normal = calcula_Normal([-2.5,3,z],[-2.5,1,z],[-1.5,1,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-2.5,3,z)
   glVertex3f(-2.5,1,z)
   glVertex3f(-1.5,1,z)
   glVertex3f(-1.5,3,z)
   glEnd()

   # Quadrante 8
   glBegin(GL_QUADS)
   #normal = calcula_Normal([1.5,1,z],[2.5,1,z],[2.5,3,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(2.5,3,z)
   glVertex3f(2.5,1,z)
   glVertex3f(1.5,1,z)
   glVertex3f(1.5,3,z)
   glEnd()

   # Quadrante 9
   glBegin(GL_QUADS)
   #normal = calcula_Normal([-4.5,1,z],[-4.5,-1,z],[-3.5,-1,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-4.5,1,z)
   glVertex3f(-4.5,-1,z)
   glVertex3f(-3.5,-1,z)
   glVertex3f(-3.5,1,z)
   glEnd()

   # Quadrante 10
   glBegin(GL_QUADS)
   #normal = calcula_Normal([3.5,-1,z],[4.5,-1,z],[4.5,1,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(4.5,1,z)
   glVertex3f(4.5,-1,z)
   glVertex3f(3.5,-1,z)
   glVertex3f(3.5,1,z)
   glEnd()

   # Quadrante 11
   glBegin(GL_QUADS)
   #normal = calcula_Normal([-5.5,0,-1,z],[-5.5,-3,-1,z],[-4.5,-3,1,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-5.5,0,z)
   glVertex3f(-5.5,-3,z)
   glVertex3f(-4.5,-3,z)
   glVertex3f(-4.5,0,z)
   glEnd()

   # Quadrante 12
   glBegin(GL_QUADS)
   #normal = calcula_Normal([4.5,0,-1,z],[4.5,-3,-1,z],[5.5,-3,1,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(5.5,0,z)
   glVertex3f(5.5,-3,z)
   glVertex3f(4.5,-3,z)
   glVertex3f(4.5,0,z)
   glEnd()

   # Quadrante 13
   glBegin(GL_QUADS)
   #normal = calcula_Normal([-3.5,4,z],[-3.5,3,z],[-2.5,3,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-3.5,4,z)
   glVertex3f(-3.5,3,z)
   glVertex3f(-2.5,3,z)
   glVertex3f(-2.5,4,z)
   glEnd()

   # Quadrante 14
   glBegin(GL_QUADS)
   #normal = calcula_Normal([3.5,3,z],[3.5,4,z],[2.5,4,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(3.5,4,z)
   glVertex3f(3.5,3,z)
   glVertex3f(2.5,3,z)
   glVertex3f(2.5,4,z)
   glEnd()

   glPopMatrix()

def face_alien_B(z):
   '''

      Gera a face do alien B

   '''
   normal = []
   glPushMatrix()
   #glScalef(0.3,0.3,0)

   # Quadrante 1
   glBegin(GL_QUADS)
   normal = calcula_Normal([-1,4,z],[-1,-1,z],[1,-1,z])
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-1,4,z)
   glVertex3f(-1,-1,z)
   glVertex3f(1,-1,z)
   glVertex3f(1,4,z)
   glEnd()

   # Quadrante 2
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-1,-2,z)
   glVertex3f(1,-2,z)
   glVertex3f(1,-3,z)
   glVertex3f(-1,-3,z)
   glEnd()

   # Quadrante 3
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-4,1,z)
   glVertex3f(-2,1,z)
   glVertex3f(-2,-1,z)
   glVertex3f(-4,-1,z)
   glEnd()

   # Quadrante 4
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(4,1,z)
   glVertex3f(2,1,z)
   glVertex3f(2,-1,z)
   glVertex3f(4,-1,z)
   glEnd()

   # Quadrante 5
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-2,0,z)
   glVertex3f(-1,0,z)
   glVertex3f(-1,-4,z)
   glVertex3f(-2,-4,z)
   glEnd()

   # Quadrante 6
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(2,0,z)
   glVertex3f(1,0,z)
   glVertex3f(1,-4,z)
   glVertex3f(2,-4,z)
   glEnd()

   # Quadrante 7
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-2,1,z)
   glVertex3f(-1,1,z)
   glVertex3f(-1,3,z)
   glVertex3f(-2,3,z)
   glEnd()

   # Quadrante 8
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(2,1,z)
   glVertex3f(1,1,z)
   glVertex3f(1,3,z)
   glVertex3f(2,3,z)
   glEnd()

   # Quadrante 9
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-3,2,z)
   glVertex3f(-2,2,z)
   glVertex3f(-2,1,z)
   glVertex3f(-3,1,z)
   glEnd()

   # Quadrante 10
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(3,2,z)
   glVertex3f(2,2,z)
   glVertex3f(2,1,z)
   glVertex3f(3,1,z)
   glEnd()

   # Quadrante 11
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-3,-2,z)
   glVertex3f(-3,-3,z)
   glVertex3f(-2,-3,z)
   glVertex3f(-2,-2,z)
   glEnd()

   # Quadrante 12
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(3,-2,z)
   glVertex3f(3,-3,z)
   glVertex3f(2,-3,z)
   glVertex3f(2,-2,z)
   glEnd()

   # Quadrante 13
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(-3,-3,z)
   glVertex3f(-3,-4,z)
   glVertex3f(-4,-4,z)
   glVertex3f(-4,-3,z)
   glEnd()

   # Quadrante 14
   glBegin(GL_QUADS)
   glNormal3f(normal[0],normal[1],normal[2])
   glVertex3f(3,-3,z)
   glVertex3f(3,-4,z)
   glVertex3f(4,-4,z)
   glVertex3f(4,-3,z)
   glEnd()


   glPopMatrix()


def alien_A(x,y,z):
   # Gera invasor tipo A
   vetorFace = [[-3.5,4],[-3.5,3],[-2.5,3],[-2.5,2],[-3.5,2],[-3.5,1],[-4.5,1],[-4.5,0],
                [-5.5,0],[-5.5,-3],[-4.5,.3],[-4.5,-1],[-3.5,-1],[-3.5,-3],[-2.5,-3],
                [-2.5,-4],[-0.5,-4],[-0.5,-3],[-2.5,-3],[-2.5,-2],[2.5,-2],[2.5,-3],
                [2.5,-4],[0.5,-4],[0.5,-3],[2.5,-3],[3.5,-3],[3.5,-1],[4.5,-1],[4.5,-3],
                [5.5,-3],[5.5,0],[4.5,0],[4.5,1],[3.5,1],[3.5,2],[2.5,2],[2.5,3],[3.5,3],
                [3.5,4],[2.5,4],[2.5,3],[1.5,3],[1.5,2],[-1.5,2],[-1.5,3],[-2.5,4]
                ]
   glPushMatrix()
   glTranslatef(x,y,z)
   glScalef(0.3,0.3,0.3)
   face_alien_A(-0.5)
   face_alien_A(0.5)
   liga_Faces(vetorFace,vetorFace,-0.5,0.5)
   glPopMatrix()


def alien_B(x,y,z):
   # Gera invasor tipo B
   vetorFace = [[-1,4],[-1,3],[-2,3],[-2,2],[-3,2],[-3,1],[-4,1],[-4,-1],
                [-2,-1],[-2,-2],[-3,-2],[-3,-3],[-4,-3],[-4,-4],[-4,-3],
                [-3,-3],[-2,-3],[-2,-4],[-1,-4],[-1,-3],[1,-3],[1,-4],[2,-4],
                [2,-3],[3,-3],[3,-4],[4,-4],[4,-3],[3,-3],[3,-2],[2,-2],[2,-1],
                [4,-1],[4,1],[3,1],[3,2],[2,2],[2,3],[1,3],[1,4]
      ]
   glPushMatrix()
   glTranslatef(x,y,z)
   glScalef(0.3,0.3,0.3)
   face_alien_B(-0.5)
   face_alien_B(0.5)
   liga_Faces(vetorFace,vetorFace,-0.5,0.5)
   glPopMatrix()
