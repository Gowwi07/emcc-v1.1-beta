import warnings
import sys
import os
from gramformer import Gramformer
from contextlib import contextmanager

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Custom context manager to suppress stdout and stderr
@contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

class AutoCorrector:
    def __init__(self):  # ✅ Fixed here
        self.gf = None

    def load_model(self):
        if self.gf is None:
            with suppress_output():
                self.gf = Gramformer(models=1)

    def correct(self, text, max_candidates=1):
        self.load_model()
        corrected = list(self.gf.correct(text, max_candidates=max_candidates))
        if corrected:
            return corrected[0]
        else:
            return text

def autocorrect_input(user_input):
    corrector = AutoCorrector()
    return corrector.correct(user_input)
