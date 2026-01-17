# AWLF-Fast-ultimate
High-performance, JIT-compiled denoising engine for uncooled thermal imaging. Features 60+ FPS processing via Numba/SIMD, native 16-bit RAW support, and robust dead pixel correction. GPL-3.0 licensed; designed for industrial inspection, thermography, and embedded edge deployment.
# AWLF-Fast: Real-time Industrial Infrared Image Restoration

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)
[![Numba](https://img.shields.io/badge/Powered%20by-Numba-orange.svg)](https://numba.pydata.org/)

**AWLF-Fast** is a high-performance, JIT-compiled implementation of the Adaptive Weighted Local Fitting algorithm, designed specifically for **Uncooled Thermal Imaging (Long-wave IR)**.

Unlike the [Reference Implementation](你的MIT仓库链接), this engine is optimized for **Production Environments**.

## 🚀 Key Features

*   **⚡ Blazing Fast**: Achieves **60+ FPS** on standard CPU (i7-10th gen) for 640x512 video streams.
*   **🏭 Industrial Ready**: Native support for **16-bit RAW / TIFF** data (no dynamic range loss).
*   **🧵 Parallelized**: Fully utilizes multi-core CPUs via SIMD vectorization and OpenMP.
*   **🛡️ Robust**: Handles dead pixels (blind pixels) and stripe noise common in IR sensors.

## 📊 Performance Benchmark

| Resolution | Implementation | FPS | Latency |
| :--- | :--- | :--- | :--- |
| **640x512 (VGA)** | Pure Python (Ref) | 0.8 fps | 1250 ms |
| **640x512 (VGA)** | **AWLF-Fast** | **72 fps** | **13 ms** |
| **1280x1024 (HD)**| **AWLF-Fast** | **25 fps** | **40 ms** |

> *Tested on Intel Core i7-10750H, Single Thread vs Multi-Thread.*

## 🛠️ Installation

```bash
pip install -r requirements.txt
# Or install as a package
pip install .
