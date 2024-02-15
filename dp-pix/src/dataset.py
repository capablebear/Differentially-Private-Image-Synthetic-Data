#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import numpy as np
from PIL import Image
from .util import pillow_to_numpy

data_path = "" # 경로지정


def get_choice_path(path, file_idx): # 리스트 에서 n번째 파일을 불러온다
  files = os.listdir(path)
  try:
    print("File list: ",files)
    file = files[file_idx-1]
    print()
    path = os.path.join(path, file)
  except IndexError:
    print("please enter index smaller then file list!")
    return 0

  return path

def get_all_path(path):
    files = os.listdir(path)
    image_paths = [os.path.join(path, file) for file in files]
    return image_paths

class Dataset():
    def __init__(self, data_path, file_idx):
        self.data_dir = data_path
        self.scale = (25,25)
        self.file_idx=file_idx

    
    def get_image(self):
        image = get_choice_path(self.data_dir, self.file_idx)
        return image
    
    def get_all_image(self):
      images = get_all_path(self.data_dir)
      return images

    def load_idx_images(self):
        image_paths = set([self.get_image()])
        images = list(map(pillow_to_numpy, map(Image.open, image_paths)))
        return images

    def load_all_images(self):
        image_paths = set(self.get_all_image())
        images = list(map(pillow_to_numpy, map(Image.open, image_paths)))
        return images