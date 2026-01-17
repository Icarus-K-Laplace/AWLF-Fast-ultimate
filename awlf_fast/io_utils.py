import numpy as np
import cv2
import os

try:
    import tifffile
except ImportError:
    tifffile = None

def load_raw_16bit(filepath):
    """
    Load 16-bit industrial thermal images (TIFF/PNG/RAW).
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
        
    ext = os.path.splitext(filepath)[-1].lower()
    
    if ext in ['.tif', '.tiff']:
        if tifffile:
            img = tifffile.imread(filepath)
        else:
            # Fallback to OpenCV (might lose some tags)
            img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    else:
        img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
        
    if img is None:
        raise ValueError("Failed to load image")
        
    # Validation
    if img.dtype != np.uint16:
        print(f"Warning: Image {filepath} is {img.dtype}, expected uint16 for full dynamic range.")
        
    return img

def save_raw_16bit(filepath, img):
    """Save 16-bit image without compression loss."""
    if tifffile and filepath.endswith(('.tif', '.tiff')):
        tifffile.imwrite(filepath, img)
    else:
        cv2.imwrite(filepath, img)

def normalize_for_vis(img_16bit):
    """
    Helper to convert 16-bit RAW to 8-bit for visualization (Min-Max scaling).
    """
    min_val = np.min(img_16bit)
    max_val = np.max(img_16bit)
    if max_val == min_val:
        return np.zeros_like(img_16bit, dtype=np.uint8)
        
    norm = (img_16bit.astype(np.float32) - min_val) / (max_val - min_val)
    return (norm * 255).astype(np.uint8)
