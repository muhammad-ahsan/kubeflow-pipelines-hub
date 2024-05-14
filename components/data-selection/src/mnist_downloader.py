import numpy as np
import pandas as pd

from sklearn import datasets


def download_curate_mnist() -> pd.DataFrame:
    """
    Each datapoint is a 8x8 image of a digit.

    =================   ==============
    Classes                         10
    Samples per class             ~180
    Samples total                 1797
    Dimensionality                  64
    Features             integers 0-16
    =================   ==============
    """
    digits = datasets.load_digits()

    # Flatten the images
    n_samples: int = len(digits.images)

    # The unspecified value is inferred automatically i.e. 8 x 8 = 64
    data: np.ndarray = digits.images.reshape((n_samples, -1))

    df = pd.DataFrame(data=data, columns=digits.feature_names)
    df['target'] = digits.target
    df['target'] = df['target'].astype('int')
    return df
