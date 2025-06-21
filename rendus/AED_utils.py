# SCHIKIT-LEARN: PRE-PROCESSING
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder # Encodage des variables catégorielles ordinales
import numpy as np

def encoder_var_ordinale(df, colonnes_ordinales):
    categorical_columns = colonnes_ordinales
    ordinal_encoder = OrdinalEncoder(dtype=np.int64)
    df_enco = df.copy()

    for col in categorical_columns:
        df_enco[col] = ordinal_encoder.fit_transform(df[[col]])
    
    return df_enco