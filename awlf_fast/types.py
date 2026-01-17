from typing import Union, Tuple, Optional, NewType
import numpy as np
import numpy.typing as npt

# Define strict types for clarity and static analysis
# 8-bit image (Standard)
Image8Bit = npt.NDArray[np.uint8]

# 16-bit image (Industrial/Thermal RAW)
Image16Bit = npt.NDArray[np.uint16]

# Generic Image Type
ImageArray = Union[Image8Bit, Image16Bit]

# Configuration Dictionary
DenoiserConfig = NewType('DenoiserConfig', dict)

class ProcessingStats:
    """Struct to hold processing telemetry."""
    def __init__(self, time_ms: float, peak_mem_mb: float):
        self.time_ms = time_ms
        self.peak_mem_mb = peak_mem_mb
