import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder 

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

logging.info("Entered to Data_transformation")

sys.path = ['D:\\Projects\\Testing\\Student_Score_prediction\\src\\components', ...]
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTranformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def data_transformer_object(self):
        """
        For Data Transformation
        """

        try:
            numerical_features = [
                'writing_score',
                'reading_score'
            ]

            categorical_features = [
                'gender',
                'race_ethnicity'
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]

            numerical_pipline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('one_hot_encoder', OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )

            catigorical_pipline = Pipeline(
                steps = [
                    (('imputer', SimpleImputer(strategy = 'Most_frequent')),
                     ('one_hot_encoder', OneHotEncoder()),
                     ('scaler', StandardScaler(with_mean=False))
                     )
                ]
            )

            logging.info(f"Numerical Columns: {numerical_features}")
            logging.info(f"Categorical Columns: {categorical_features}")

            preprocessor = ColumnTransformer(
                ("Numerical_Pipeline", numerical_pipline, numerical_features),
                ("Categorical_Pipeline", catigorical_pipline, categorical_features)

            )
            logging.info("Preprocessor object created successfully")

            return preprocessor
        
        except Exception as e:
            logging.info("Error in creating preprocessor object")
            raise CustomException(e, sys)
            


    def initiate_data_transformation(self, train_path, test_path):
        logging.info("Data Transformation initiated")

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and Test data read as Pandas DataFrame")

            preprocessing_obj = self.data_transformer_object()
            target_column_name = "math_score"

            numerical_features = [
                'writing_score',
                'reading_score'
            ]

            input_feature_train_df = train_df.drop(columns = [target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(column = [target_column_name])
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Preprocessing the training and testing Data Frame."
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Preprocessed object saved...")

            save_object(
                    file_path=self.data_transformation_config.preprocessor_obj_file_path,
                    obj = preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.info("Error in reading train data")
            raise CustomException(e, sys)