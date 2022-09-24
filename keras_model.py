########################################################################
# import python-library
########################################################################
# from import
import keras.models
from keras import backend as K
from keras import regularizers
from keras.layers import Input, Dense, BatchNormalization, Activation, Conv2D, PReLU, Flatten, MaxPool2D, Dropout
from keras.models import Model
import tensorflow as tf
import tensorflow_addons as tfa

########################################################################
# keras model
########################################################################
def get_model(input_dim, lr):
    """
    define the keras model
    the model based on the simple dense auto encoder 
    (128*128*128*128*8*128*128*128*128)
    """

def get_model(input_dim, lr):
    """
    define the keras model
    the model based on the simple dense auto encoder 
    (128*128*128*128*8*128*128*128*128)
    """
    regularizer = regularizers.L2(1e-4)
    x = Input(shape=(input_dim,))

    h = Dense(128, kernel_regularizer=regularizer)(x)
    h = BatchNormalization()(h)
    h = PReLU()(h)

    h = Dense(128, kernel_regularizer=regularizer)(h)
    h = BatchNormalization()(h)
    h = PReLU()(h)

    h = Dense(128, kernel_regularizer=regularizer)(h)
    h = BatchNormalization()(h)
    h = PReLU()(h)

    h = Dense(128, kernel_regularizer=regularizer)(h)
    h = BatchNormalization()(h)
    h = PReLU()(h)

    h = Dense(8)(h)
    h = BatchNormalization()(h)
    h = PReLU()(h)
    
    h = Dense(128, kernel_regularizer=regularizer)(h)
    h = BatchNormalization()(h)
    h = PReLU()(h)

    h = Dense(128, kernel_regularizer=regularizer)(h)
    h = BatchNormalization()(h)
    h = PReLU()(h)

    h = Dense(128, kernel_regularizer=regularizer)(h)
    h = BatchNormalization()(h)
    h = PReLU()(h)

    h = Dense(128, kernel_regularizer=regularizer)(h)
    h = BatchNormalization()(h)
    h = PReLU()(h)

    h = Dense(input_dim)(h)

    model = Model(inputs=x, outputs=h)

    model.compile(optimizer=tfa.optimizers.AdamW(weight_decay=lr), 
                  loss='mean_squared_error')

    return model

#########################################################################

def load_model(file_path):
    return keras.models.load_model(file_path, compile=False)

def clear_session():
    K.clear_session()
    