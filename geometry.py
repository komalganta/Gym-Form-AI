import numpy as np

class PoseGeometry:
    @staticmethod
    def calculate_angle(p1, p2, p3):
        """Calculates the angle at p2 (vertex) using 3D coordinates."""
        # Convert landmarks to numpy arrays for better vector math
        a, b, c = np.array(p1), np.array(p2), np.array(p3)

        # Create vectors meeting at joint b
        ba = a - b
        bc = c - b

        # Use dot product to find angle
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))
        
        return angle