import numpy as np
import cv2

import content._static.local_codebase.imports.utils as ut
from content._static.local_codebase.imports.utils import LogType


class SystematicNavigator:
    '''
    Systematic navigator class. \
    Used as a base class for navigators that \
    extract data from the environment map, then plan a path.
    '''
    def __init__(
        self,
        resolution=0.1,
        map_resolution=0.05,
        lethal_threshold=20.0
    ):
        self.navigator_type = "systematic"
        self.paths = None
        self.map = None
        self.polymap = None
        self.threshold = lethal_threshold
        self.resolution = resolution
        self.map_resolution = map_resolution
        self.node = None

    def plan(self, new_map, start: np.ndarray = np.zeros(2), show=False) -> None:
        self.start = start
        self.update_map(new_map, show)
        self.generate_path()

    def update_map(self, new_map):
        self.map = new_map

        self.binary_costmap = np.zeros_like(self.map, dtype=np.uint8)
        self.binary_costmap[self.map < self.threshold] = 255
        self.binary_costmap[self.map == -1] = 0

        margin_m = 0.3
        margin_px = max(1, int(margin_m / self.map_resolution))

        if margin_px % 2 == 0:
            margin_px += 1

        contours, _ = cv2.findContours(
            self.binary_costmap, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = [
            cv2.approxPolyDP(c, 0.005 * cv2.arcLength(c, True), True) for c in contours
        ]
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        outer_contour = contours[0]

        # Filter out contours that lie outside the largest contour
        filtered_contours = [outer_contour]

        for contour in contours[1:]:  # skip outer
            if len(contour) < 4:
                ut.log(
                    self.node,
                    LogType.WARN,
                    f"Skipping contour with {len(contour)} points",
                )
                continue
            filtered_contours.append(contour)

        self.contours = filtered_contours

        closed_contour = []
        for contour in filtered_contours:
            pts = contour[:, 0, :]

            self.map_height = self.map.shape[0]
            self.map_width = self.map.shape[1]

            points = [
                (
                    (px - 0.5 * self.map_width) * self.map_resolution,
                    (py - 0.5 * self.map_height) * self.map_resolution,
                )
                for px, py in pts
            ]

            if points[0] != points[-1]:
                points.append(points[0])

            closed_contour.append(points)

        self.polymap = closed_contour
        return None

    def is_inside(self, contour, outer_contour):
        for pt in contour[:, 0, :]:
            # returns >0 inside, 0 on edge, <0 outside
            if (
                cv2.pointPolygonTest(outer_contour, (float(pt[0]), float(pt[1])), False)
                < 0
            ):
                return False
        return True

    def world_to_pixel(self, polygon):
        map_h, map_w = self.map.shape[:2]

        coords = []
        for coord in polygon:
            px = int(coord[0] / self.map_resolution + 0.5 * map_w)
            py = int(coord[1] / self.map_resolution + 0.5 * map_h)
            coords.append([px, py])

        return np.array(coords, dtype=np.int32)

    def world_to_pixel_path(self, path):
        map_h, map_w = self.map.shape[:2]

        pts = np.array(path)

        pts[:, 0] = pts[:, 0] / self.map_resolution + 0.5 * map_w
        pts[:, 1] = pts[:, 1] / self.map_resolution + 0.5 * map_h

        return pts.astype(np.int32)


class ReactiveNavigator:
    def __init__(self):
        self.navigator_type = "reactive"
