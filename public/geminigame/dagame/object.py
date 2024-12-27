# dagame/object.py
# object.py adjusted for engVector usage
from vec_ops.vector import engVector
from vec_ops.physics import apply_force

class Object:
    """
    Represents a generic game object with physical properties and behaviors.
    """

    def __init__(self, x, y, width, height, mass):
        """
        Initializes a new game object with position, size, and mass.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mass = max(mass, 1)  # Ensure mass is positive, non-zero
        self.velocity = engVector.create_vector(0.0, 0.0)
        self.acceleration = engVector.create_vector(0.0, 0.0)

    def update_position(self, dt):
        """
        Updates the object's position based on its velocity and acceleration.
        """
        self.velocity = engVector.add_vectors(self.velocity, engVector.multiply_vector(self.acceleration, dt))
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt
        self.acceleration = engVector.create_vector(0.0, 0.0)  # Reset acceleration

    def apply_force(self, force):
        """
        Applies a force to the object, affecting its acceleration.
        """
        force_vector = engVector.create_vector(force[0], force[1])
        self.acceleration = engVector.add_vectors(self.acceleration, engVector(values=[force_vector[0] / self.mass, force_vector[1] / self.mass]))
