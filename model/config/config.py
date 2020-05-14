import pathlib

import model

PACKAGE_ROOT = pathlib.Path(model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_model"

GENDER_MODEL_NAME = "model_gender-"
AGE_MODEL_NAME = "model_age-"
COUNTRY_MODEL_NAME = "model_country-"

FRAME_RATE = 48000
OBSERVATION_PER_SECOND = 10
SEQ_LEN = FRAME_RATE / OBSERVATION_PER_SECOND


class Bucket:
    RAW_DATA = "common-voice-voice-all"
    META_DATA = "common-voice-voice-data"
    VALIDATION_SET = "common-voice-voice-dev"
    TEST_SET = "common-voice-voice-test"
    TRAIN_SET = "common-voice-voice-train"


class Model:
    OUTPUT_SIZE = 2
    HIDDEN_DIM = 512
    NUM_LAYERS = 10
    DROPOUT = 0.30
    INPUT_SIZE = 648
    BATCH_SIZE = 256


class Train:
    LEARNING_RATE = 0.00001
    GRADIENT_CLIP = 1
    EPOCH = 10


class GCP_Storage:
    CLIPS_DIR = "/home/jupyter/clips"
    ROOT_DIR = "/home/jupyter/"
    DEV_DIR = "/home/jupyter/common-voice-voice-train"


class GCP_Train_Pipeline:
    TRAIN_DIR = "/home/jupyter/wav/gender/train_data"
    VAL_DIR = "/home/jupyter/wav/gender/val_data"
    TEST_DIR = "/home/jupyter/wav/gender/test_data"


class Local_Storage:
    WAV_DIR = r"C:\Users\ander\Documents\common-voice-data\wav"
    ROOT_DIR = r"C:\Users\ander\Documents\common-voice-data"
    DEV_DIR = r"C:\Users\ander\Documents\common-voice-dev"
    CLIPS_DIR = r"C:\Users\ander\Documents\common-voice-data\clips"
    TRAIN_DIR = r"C:\Users\ander\Documents\common-voice-dev"


class Local_Train_Pipeline:
    TRAIN_DIR = r"C:\Users\ander\Documents\common-voice-dev\gender\train_data"
    VAL_DIR = r"C:\Users\ander\Documents\common-voice-dev\gender\val_data"
    TEST_DIR = r"C:\Users\ander\Documents\common-voice-dev\gender\test_data"
