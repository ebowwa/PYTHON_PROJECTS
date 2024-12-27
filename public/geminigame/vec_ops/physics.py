# vec_ops/physics.py
from .vector import engVector
from typing import Union

def apply_force(acceleration: Union[int, float], force: Union[int, float], mass: Union[int, float]) -> float:
    return acceleration + (force / mass)