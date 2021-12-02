import struct
import cv2
import numpy as np

def serialize(img):
    return struct.pack('iii', *img.shape) + img.tobytes()

def unserialize(data):
    tag_size = struct.calcsize('iii')
    shape = struct.unpack('iii', data[:tag_size])
    frame = np.frombuffer(data[tag_size:], dtype=np.uint8)
    frame = frame.reshape(shape)
    return frame
