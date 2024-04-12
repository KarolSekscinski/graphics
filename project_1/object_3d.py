import pygame as pg
from matrix_operations import *


class Object3D:
    def __init__(self, render):
        self.render = render
        self.vertexes = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                  (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1),

                                  (0, 0, 2, 1), (0, 2, 2, 1), (1, 2, 2, 1), (1, 0, 2, 1),
                                  (0, 0, 3, 1), (0, 2, 3, 1), (1, 2, 3, 1), (1, 0, 3, 1),

                                  (2, 0, 0, 1), (2, 1, 0, 1), (3, 1, 0, 1), (3, 0, 0, 1),
                                  (2, 0, 1, 1), (2, 1, 1, 1), (3, 1, 1, 1), (3, 0, 1, 1),

                                  (2, 0, 2, 1), (2, 2, 2, 1), (3, 2, 2, 1), (3, 0, 2, 1),
                                  (2, 0, 3, 1), (2, 2, 3, 1), (3, 2, 3, 1), (3, 0, 3, 1)])

        self.faces = np.array([(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4),
                               (8, 9, 10, 11), (12, 13, 14, 15), (8, 12, 13, 9), (10, 11, 15, 14), (9, 10, 14, 13),
                               (8, 11, 15, 12),
                               (16, 17, 18, 19), (20, 21, 22, 23), (16, 20, 21, 17), (18, 19, 23, 22), (17, 18, 22, 21),
                               (16, 19, 23, 20),
                               (24, 25, 26, 27), (28, 29, 30, 31), (24, 28, 29, 25), (26, 27, 31, 30), (25, 26, 30, 29),
                               (24, 27, 31, 28)])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        # multiply vertexes in order to postion and orients the 3D object
        # relative to the camera
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        # multiply the 3D vertexes by the projection matrix to get the 4D vertexes (homogeneus coordinates)
        vertexes = vertexes @ self.render.projection.projection_matrix
        # divide the homogeneous coordinate by the w component in order to
        # get the x, y, z coordinates in the Normalizewd Device Coordinate (NDC)
        # vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes /= vertexes[:, [-1]]
        # throw out the vertexes which are further away than 2.0 distance
        # vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        # multiply the vertexes by the to_screen_matrix to get the actual screen coordinates
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]

        # show faces
        for face in self.faces:
            polygon = vertexes[face]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                pg.draw.polygon(self.render.screen, pg.Color('gray'), polygon, 3)

        # show vertexes
        for vertex in vertexes:
            if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)

    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)

    def scale(self, scale_to):
        self.vertexes = self.vertexes @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertexes = self.vertexes @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertexes = self.vertexes @ rotate_z(angle)