import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def drawCar():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10)
    #glBegin(GL_POINTS)
    #glBegin(GL_LINES)
    #glBegin(GL_LINE_STRIP)
    glBegin(GL_LINE_LOOP)

   
    glVertex2f(-0.5, 0.0)
    glVertex2f(-0.5,0.2)
    glVertex2f(-0.3,0.5)
    glVertex2f(0.3,0.5)
    glVertex2f(0.3,0.2)
    glVertex2f(0.7,0.2)
    glVertex2f(0.7,0.0)
    glVertex2f(0.3,0.0)
    
    glVertex2f(0.3,0.2)
    
    glVertex2f(0.3,0.0)





    

    glEnd()
    glFlush()


    
def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        drawCar()
        pygame.display.flip()
        pygame.time.wait(10)
        
   
main()
