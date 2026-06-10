import numpy as np

class ModelValidator:

    @staticmethod
    def validate_predictions(predictions):
        assert not np.any(np.isnan(predictions))
        assert not np.any(np.isinf(predictions))
        print("✓ Predictions valides")

    @staticmethod
    def validate_binary(predictions):
        unique = set(predictions)
        assert unique.issubset({0, 1})
        print("✓ Classification binaire valide")