from enum import Enum


class Parameter(Enum):
    EMBEDDINGS = "embeddings"
    HIDDEN_SIZE = "hidden_size"
    USE_CRF = "use_crf"
    USE_RNN = "use_rnn"
    RNN_LAYERS = "rnn_layers"
    DROPOUT = "dropout"
    WORD_DROPOUT = "word_dropout"
    LOCKED_DROPOUT = "locked_dropout"
    LEARNING_RATE = "learning_rate"
    MINI_BATCH_SIZE = "mini_batch_size"
    ANNEAL_FACTOR = "anneal_factor"
    ANNEAL_WITH_RESTARTS = "anneal_with_restarts"
    PATIENCE = "patience"
    REPROJECT_WORDS = "reproject_words"
    REPROJECT_WORD_DIMENSION = "reproject_words_dimension"
    BIDIRECTIONAL = "bidirectional"
    OPTIMIZER = "optimizer"
    MOMENTUM = "momentum"
    DAMPENING = "dampening"
    WEIGHT_DECAY = "weight_decay"
    NESTEROV = "nesterov"
    AMSGRAD = "amsgrad"
    BETAS = "betas"
    EPS = "eps"
    GIT = "GET"


TRAINING_PARAMETERS = [
    Parameter.LEARNING_RATE.value,
    Parameter.MINI_BATCH_SIZE.value,
    Parameter.ANNEAL_FACTOR.value,
    Parameter.PATIENCE.value,
    Parameter.ANNEAL_WITH_RESTARTS.value,
    Parameter.MOMENTUM.value,
    Parameter.DAMPENING.value,
    Parameter.WEIGHT_DECAY.value,
    Parameter.NESTEROV.value,
    Parameter.AMSGRAD.value,
    Parameter.BETAS.value,
    Parameter.EPS.value,
]
SEQUENCE_TAGGER_PARAMETERS = [
    Parameter.EMBEDDINGS.value,
    Parameter.HIDDEN_SIZE.value,
    Parameter.RNN_LAYERS.value,
    Parameter.USE_CRF.value,
    Parameter.USE_RNN.value,
    Parameter.DROPOUT.value,
    Parameter.LOCKED_DROPOUT.value,
    Parameter.WORD_DROPOUT.value,
]
MODEL_TRAINER_PARAMETERS = [Parameter.OPTIMIZER.value]
DOCUMENT_EMBEDDING_PARAMETERS = [
    Parameter.EMBEDDINGS.value,
    Parameter.HIDDEN_SIZE.value,
    Parameter.RNN_LAYERS.value,
    Parameter.REPROJECT_WORDS.value,
    Parameter.REPROJECT_WORD_DIMENSION.value,
    Parameter.BIDIRECTIONAL.value,
    Parameter.DROPOUT.value,
    Parameter.LOCKED_DROPOUT.value,
    Parameter.WORD_DROPOUT.value,
]
