import numpy as np
import time
import os
import sys
from memory_profiler import profile

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from awlf_fast import FastDenoiser

# Simulate a 4K 16-bit Thermal Sensor Stream (3840x2160)
H, W = 2160, 3840
DTYPE = np.uint16

@profile(precision=4)
def stress_test_memory_leak():
    """
    Simulates continuous processing to detect memory leaks.
    Target: Memory usage should remain stable (flatline) after warmup.
    """
    print(f"--- Starting Memory Stress Test ---")
    print(f"Resolution: {W}x{H} (16-bit RAW)")
    
    # Initialize Engine
    denoiser = FastDenoiser()
    denoiser.warmup()
    
    # Simulate 50 frames batch
    # We create new random arrays to simulate incoming sensor data
    # (forcing GC to work hard)
    for i in range(50):
        # 16MB per frame
        frame = np.random.randint(0, 65535, (H, W), dtype=DTYPE)
        _ = denoiser.process(frame)
        
        if i % 10 == 0:
            print(f"Processed frame {i}/50...")

if __name__ == "__main__":
    print("Note: Install 'memory_profiler' to run this test.")
    stress_test_memory_leak()
