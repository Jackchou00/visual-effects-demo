import numpy as np

def f(t):
    delta = 6/29
    return np.where(t > delta**3, t**(1/3), (1/3)*(29/6)**2 * t + 4/29)

def xyz2lab_DW(xyz, DW):
    img_height = xyz.shape[0]
    img_width = xyz.shape[1]
    xyz_reshaped = xyz.reshape(-1, 3)
    
    # Calculate f(X/DW[0]), f(Y/DW[1]), and f(Z/DW[2])
    fX = f(xyz_reshaped[:, 0] / DW[0])
    fY = f(xyz_reshaped[:, 1] / DW[1])
    fZ = f(xyz_reshaped[:, 2] / DW[2])
    
    # Calculate L, a, and b
    L = 116 * fY - 16
    a = 500 * (fX - fY)
    b = 200 * (fY - fZ)
    
    # Combine into Lab format
    lab = np.stack([L, a, b], axis=-1)
    lab = lab.reshape(img_height, img_width, 3)
    
    return lab

def inv_f(t):
    delta = 6 / 29
    return np.where(t > delta, t**3, 3 * (delta**2) * (t - 4/29))

def lab2xyz_SDRW(lab, SDRW):
    img_height = lab.shape[0]
    img_width = lab.shape[1]
    lab_reshaped = lab.reshape(-1, 3)
    
    L = lab_reshaped[:, 0]
    a = lab_reshaped[:, 1]
    b = lab_reshaped[:, 2]
    
    # Calculate fY, fX, and fZ
    fY = (L + 16) / 116
    fX = fY + a / 500
    fZ = fY - b / 200
    
    # Convert fX, fY, fZ to X, Y, Z
    X = SDRW[0] * inv_f(fX)
    Y = SDRW[1] * inv_f(fY)
    Z = SDRW[2] * inv_f(fZ)
    
    # Combine into XYZ format
    xyz = np.stack([X, Y, Z], axis=-1)
    xyz = xyz.reshape(img_height, img_width, 3)
    
    return xyz

