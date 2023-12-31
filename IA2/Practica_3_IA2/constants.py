NORMALIZATION_RANGE = -1.0, 1.0
LEARNING_RATE = 0.2
MAX_EPOCHS = 30
DESIRED_ERROR = 0.1

FIG_WIDTH = 13
FIG_HEIGHT = 6
SUBPLOT_ROWS = 1
SUBPLOT_COLS = 2
FIG_SUPERIOR_TITLE = "Adaline training algorithm"
MAIN_SUBPLOT_PERCEPTRON_TITLE = "Adaline"
PERCEPTRON_ERRORS_SUBPLOT_TITLE = "Error Graph"
ADALINE_ERRORS_SUBPLOT_TITLE = "Adaline cumulative error"
ERRORS_SUBPLOT_XLABEL = "Epochs"
PERCEPTRON_ERRORS_SUBPLOT_YLABEL = "No. of errors"
ADALINE_ERRORS_SUBPLOT_YLABEL = "E²"

MAIN_SUBPLOT_PAUSE_INTERVAL = 0.1
MAIN_SUBPLOT_ADALINE_PAUSE_INTERVAL = 0.0125
ERRORS_SUBPLOT_PAUSE_INTERVAL = 0.3

ALGORITHM_CONVERGED_TEXT = 'Algorithm converged'
ALGORITHM_DIDNT_CONVERGE_TEXT = "Algorithm couldn't converge"
PERCEPTRON_CONVERGENCE_TEXT_FONT_SIZE = 10
PERCEPTRON_CONVERGENCE_TEXT_X_POS = -0.25
PERCEPTRON_CONVERGENCE_TEXT_Y_POS = 0.9
CONVERGENCE_OFFSET = 0.25

CURRENT_EPOCH_TEXT = 'Epoch: %s'
CURRENT_EPOCH_TEXT_FONT_SIZE = 10
CURRENT_EPOCH_TEXT_X_POS = 0.5
CURRENT_EPOCH_TEXT_Y_POS = 0.8

CLASS_0_MARKER = 'bx'
CLASS_1_MARKER = 'r.'
CLASS_0_MARKER_POST_PERCEPTRON_FIT = 'kx'
CLASS_1_MARKER_POST_PERCEPTRON_FIT = 'k.'
CLASS_0_MARKER_POST_ADALINE_FIT = 'gx'
CLASS_1_MARKER_POST_ADALINE_FIT = 'g.'
PERCEPTRON_DECISION_BOUNDARY_MARKER = 'y-'
ADALINE_DECISION_BOUNDARY_MARKER = 'm-'

TEXT_BOX_LEARNING_RATE_AXES = [0.2, 0.15, 0.175, 0.05]
TEXT_BOX_LEARNING_RATE_PROMPT = "Learning rate (η):"
TEXT_BOX_MAX_EPOCHS_AXES = [0.5, 0.15, 0.15, 0.05]
TEXT_BOX_MAX_EPOCHS_PROMPT = "Max no. of epochs:"
TEXT_BOX_DESIRED_ERROR_AXES = [0.75, 0.15, 0.15, 0.05]
TEXT_BOX_DESIRED_ERROR_PROMPT = "Desired error:"
BUTTON_WEIGHTS_AXES = [0.225, 0.05, 0.125, 0.05]
BUTTON_WEIGHTS_TEXT = "Initialize Weights"
BUTTON_PERCEPTRON_AXES = [0.4625, 0.05, 0.1, 0.05]
BUTTON_PERCEPTRON_TEXT = "Adaline"