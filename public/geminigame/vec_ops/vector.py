# vec_ops/vector.py
from pydantic import BaseModel, validator
from typing import List, Union
import numpy as np
import math
import pandas as pd

class engVector(BaseModel):
    values: List[Union[int, float]]

    @validator('values')
    def check_length(cls, v):
        if len(v) != 2:
            raise ValueError('Vector must have exactly 2 elements')
        return v

    def to_numpy(self) -> np.ndarray:
        return np.array(self.values)

    def to_pandas(self) -> pd.Series:
        return pd.Series(self.values, index=["x", "y"])

    def magnitude(self) -> float:
        return math.sqrt(sum([x**2 for x in self.values]))

    def __add__(self, other: "engVector") -> "engVector":
        if not isinstance(other, engVector):
            raise TypeError(f"Unsupported operand type(s) for +: 'engVector' and '{type(other).__name__}'")
        return engVector(values=(self.to_numpy() + other.to_numpy()).tolist())

    def __getitem__(self, key):
        return self.values[key]

    def __truediv__(self, scalar: Union[int, float]) -> 'engVector':
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return engVector(values=[value / scalar for value in self.values])

    @staticmethod
    def create_vector(x: Union[int, float], y: Union[int, float]) -> 'engVector':
        return engVector(values=[x, y])

    @staticmethod
    def add_vectors(v1: "engVector", v2: "engVector") -> "engVector":
        np_v1 = v1.to_numpy()
        np_v2 = v2.to_numpy()
        return engVector(values=(np_v1 + np_v2).tolist())

    @staticmethod
    def multiply_vector(v: "engVector", scalar: Union[int, float]) -> "engVector":
        np_v = v.to_numpy()
        return engVector(values=(np_v * scalar).tolist())

    def angle_with(self, other: "engVector") -> float:
        dot_product = np.dot(self.to_numpy(), other.to_numpy())
        magnitudes = self.magnitude() * other.magnitude()
        if magnitudes == 0:
            raise ValueError("Cannot calculate angle with zero magnitude vector")
        angle_radians = math.acos(dot_product / magnitudes)
        return math.degrees(angle_radians)
