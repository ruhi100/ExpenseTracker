from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.4, 0.4, 0.4, 1.0)
    glEnable(GL_DEPTH_TEST)


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -5)

    # Cube
    glColor3f(1, 0, 0)
    glutSolidCube(2)

    glutSwapBuffers()


def update(value):
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 400)
    glutCreateWindow(b"IDLE OpenGL Window")

    init()

    glutDisplayFunc(draw)
    glutTimerFunc(16, update, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()



