import math
import open3d as o3d
import numpy as np
from plane.plane import Plane
from point_cloud.point_cloud import Point_cloud

class Angle:
    def calculate_angles(a1, b1, c1, a2, b2, c2):
        """Calculates the angle between two planes:\n
        \ta1 * x + b1 * y + c1 * z + d1 = 0 \n
        and \n
        \ta2 * x + b2*y + c2 * z + d2 = 0"""
        temp = (a1 * a2 + b1 * b2 + c1 * c2)
        e1 = math.sqrt(a1 * a1 + b1 * b1 + c1 * c1)
        e2 = math.sqrt(a2 * a2 + b2 * b2 + c2 * c2)
        temp = temp / (e1 * e2)
        angle = math.degrees(math.acos(temp))

        print(f'The angle is {angle} degrees')
        print("")
        return angle
    
    def calculate_leaf_angle(stem_plane_a, stem_plane_b, stem_plane_c, filename):
        pc_leaf = o3d.io.read_point_cloud(filename)
        # pc_leaf.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=10))

        # distances = pc_leaf.compute_nearest_neighbor_distance()
        # avg_dist = np.mean(distances)
        # radius = 1.5 * avg_dist   
        # mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        #        pc_leaf,
        #        o3d.utility.DoubleVector([radius, radius * 2]))

        # np_triangles = np.asanyarray(mesh.triangles)
        # for line in np_triangles:
        #     print(line)

        # Calculate angles
        print("")
        print(f'"\033[4mCalculating angle {filename}\033[0m"')

        line_np_points = np.asarray(pc_leaf.points)
        line_np_normals = np.asarray(pc_leaf.normals)
        
        leaf_plane_a, leaf_plane_b, leaf_plane_c, leaf_plane_d = Plane.get_plane(Point_cloud.array_to_point_cloud_with_normals(line_np_points, line_np_normals))

        Angle.calculate_angles(stem_plane_a, stem_plane_b, stem_plane_c, leaf_plane_a, leaf_plane_b, leaf_plane_c)
