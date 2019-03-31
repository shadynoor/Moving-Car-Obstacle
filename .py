from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

def drawXYZ():

    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex(0,0,0)
    glVertex(0,10,0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex(0,0,0)
    glVertex(10,0,0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex(0,0,0)
    glVertex(0,0,10)
    glEnd()


angle = 0
trans = 0
right = True
def draw():
    global angle
    global trans
    global right



    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotate(90,0,1,0)
    glClearColor(.1,.1,.1, 1)
    glClear(GL_COLOR_BUFFER_BIT)



    glBegin(GL_POLYGON)
    glColor3f(.3, .3, .3)
    glVertex(50,0,6)
    glVertex(60,0,-6)
    glVertex(-60,0,-6)
    glVertex(-50,0,6)
    glEnd()


    glColor3f(1, 0, 0)
    glTranslate(trans,0,z)
    glScale(1,.25,.5)
    glutSolidCube(5)
    glLoadIdentity()
    glColor3f(0, 0, 0)

    glRotate(90,0,1,0)
    glTranslate(trans,0,0)
    glTranslated(0,5*.25,z)
    glScale(.5, .25, .5)
    glutSolidCube(5)
    glLoadIdentity()

    glRotate(90,0,1,0)
    glColor3f(0, 0, 0)
    glTranslate(trans,0,0)
    glTranslated(2.5,-5*.25*.5,5*.5*.5+z)
    glRotate(angle,0,0,1)
    glutSolidTorus(.125, .5, 12, 10)
    glLoadIdentity()


    glRotate(90,0,1,0)
    glColor3f(0, 0, 0)
    glTranslate(trans,0,0)
    glTranslated(-2.5,-5*.25*.5,5*.5*.5+z)
    glRotate(angle,0,0,1)
    glutSolidTorus(.125, .5, 12, 10)
    glLoadIdentity()

    glRotate(90,0,1,0)
    glColor3f(0, 0, 0)
    glTranslate(trans,0,0)
    glTranslated(2.5,-5*.25*.5,-5*.5*.5+z)
    glRotate(angle,0,0,1)
    glutSolidTorus(.125, .5, 12, 10)
    glLoadIdentity()

    glRotate(90,0,1,0)
    glColor3f(0, 0, 0)
    glTranslate(trans,0,0)
    glTranslated(-2.5,-5*.25*.5,-5*.5*.5+z)
    glRotate(angle,0,0,1)
    glutSolidTorus(.125, .5, 12, 10)
    glLoadIdentity()



    glRotate(90,0,1,0)
    glColor3f(0, 0, 1)
    glTranslate(-trans,0,0)
    glTranslated(2.5,-5*.25*.5,-5*.5*.5)
    glRotate(angle,0,0,1)
    glutWireSphere(1.5,20,20)
    glLoadIdentity()





    glutSwapBuffers()
    if right == True:
        if trans < 9:
            angle -= .1
            trans += .01
        else:
            right = False
    elif right == False:
        if trans > -9:
            angle+=.1
            trans-=.01
        else:
            right = True



z = 0
def specialKeyHandler(key,x,y):
    global z
    if key == GLUT_KEY_RIGHT:
        z=z+.1
    elif key == GLUT_KEY_LEFT:
        z=z-.1

    draw()







glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(specialKeyHandler)
glutMainLoop()
