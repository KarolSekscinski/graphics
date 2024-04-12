import math
import numpy as np


class Projection:
    def __init__(self, render):
        self.aspect_ratio = render.WIDTH / render.HEIGHT
        NEAR = render.camera.near_plane
        FAR = render.camera.far_plane
        RIGHT = math.tan(render.camera.h_fov / 2)
        LEFT = -RIGHT
        TOP = math.tan(render.camera.v_fov / 2)
        BOTTOM = -TOP
        self.render = render

        # creating the matrix which will transform the 3D points
        # from the camera space to the homogeneous coordinates
        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        # creating the matrix which will transform the NCD points
        # into actual screen coordinates
        HW, HH = render.H_WIDTH, render.H_HEIGHT
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])

    def update_projection_matrix(self):
        NEAR = self.render.camera.near_plane
        FAR = self.render.camera.far_plane
        RIGHT = math.tan(self.render.camera.h_fov / 2)
        LEFT = -RIGHT
        TOP = RIGHT / self.aspect_ratio
        BOTTOM = -TOP

        # creating the matrix which will transform the 3D points
        # from the camera space to the homogeneous coordinates
        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])
