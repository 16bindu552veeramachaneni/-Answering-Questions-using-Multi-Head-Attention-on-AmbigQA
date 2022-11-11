import string
import re
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import re
import torch
import torch.nn as nn
import torch.optim as optim

import torchtext
from torchtext import data
from torchtext.data import Field, BucketIterator

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import spacy
import numpy as np

import random
import math
import time
import pandas as pd
path = 'C:\\Users\\bindu\\Desktop\\M.tech\\Major Project M.tech\\ambignq'
df = pd.read_json(path, lines=False, orient=str)
df.shape
