import pandas as pd
import numpy as np


chat_id = 307311223  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x_ = x - 263
    a = sum(np.log(x_))/len(x)
    return a
