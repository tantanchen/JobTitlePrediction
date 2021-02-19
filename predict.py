import pandas as pd
import numpy as np
import tensorflow as tf
import io, codecs
import fasttext
import fasttext.util
from pydantic import BaseModel
from fastapi import FastAPI
from tensorflow import keras
from sklearn.metrics.pairwise import cosine_similarity
from keras.preprocessing import sequence
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
