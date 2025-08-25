<!-- done all the steps -->

### Network Security Projects For Phising Data

Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = 
ECR_REPOSITORY_NAME = 

Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker


### Project: Data Pipeline with DVC and MLflow for Machine Learning
This project demonstrates how to build an end-to-end machine learning pipeline using DVC (Data Version Control) for data and model versioning, and MLflow for experiment tracking. The pipeline focuses on training a Random Forest Classifier on the Pima Indians Diabetes Dataset, with clear stages for data preprocessing, model training, and evaluation.

Key Features of the Project:
Data Version Control (DVC):

DVC is used to track and version the dataset, models, and pipeline stages, ensuring reproducibility across different environments.
The pipeline is structured into stages (preprocessing, training, evaluation) that can be automatically re-executed if any dependencies change (e.g., data, scripts, or parameters).
DVC also allows remote data storage (e.g., DagsHub, S3) for large datasets and models.
Experiment Tracking with MLflow:

MLflow is used to track experiment metrics, parameters, and artifacts.
It logs the hyperparameters of the model (e.g., n_estimators, max_depth) and performance metrics like accuracy.
MLflow helps compare different runs and models to optimize the machine learning pipeline.
Pipeline Stages:
Preprocessing:

The preprocess.py script reads the raw dataset (data/raw/data.csv), performs basic preprocessing (such as renaming columns), and outputs the processed data to data/processed/data.csv.
This stage ensures that data is consistently processed across runs.
Training:

The train.py script trains a Random Forest Classifier on the preprocessed data.
The model is saved as models/random_forest.pkl.
Hyperparameters and the model itself are logged into MLflow for tracking and comparison.
Evaluation:

The evaluate.py script loads the trained model and evaluates its performance (accuracy) on the dataset.
The evaluation metrics are logged to MLflow for tracking.
Goals:
Reproducibility: By using DVC, the pipeline ensures that the same data, parameters, and code can reproduce the same results, making the workflow reliable and consistent.
Experimentation: MLflow allows users to easily track different experiments (with varying hyperparameters) and compare the performance of models.
Collaboration: DVC and MLflow enable smooth collaboration in a team environment, where different users can work on the same project and track changes seamlessly.
Use Cases:
Data Science Teams: Teams can use this project setup to track datasets, models, and experiments in a reproducible and organized manner.
Machine Learning Research: Researchers can quickly iterate over different experiments, track performance metrics, and manage data versions effectively.
Technology Stack:
Python: The core programming language for data processing, model training, and evaluation.
DVC: For version control of data, models, and pipeline stages.
MLflow: For logging and tracking experiments, metrics, and model artifacts.
Scikit-learn: For building and training the Random Forest Classifier.
This project demonstrates how to manage the lifecycle of a machine learning project, ensuring that data, code, models, and experiments are all tracked, versioned, and reproducible.

### For Adding DVC Pipeline Stages :

dvc init

dvc stage add -n data_ingestion \
    -d networksecurity/components/data_ingestion.py \
    -d networksecurity/entity/config_entity.py \
    -d networksecurity/constants/training_pipeline/__init__.py \
    -d networksecurity/utils/common.py \
    -o Artifacts/data_ingestion \
    python -c "from networksecurity.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig; from networksecurity.components.data_ingestion import DataIngestion; cfg=TrainingPipelineConfig(); DataIngestion(DataIngestionConfig(cfg)).initiate_data_ingestion();"

	
	
dvc stage add -n data_validation \
    -d Artifacts/data_ingestion \
    -d data_schema/schema.yaml \
    -d networksecurity/components/data_validation.py \
    -d networksecurity/entity/config_entity.py \
    -d networksecurity/constants/training_pipeline/__init__.py \
    -d networksecurity/utils/common.py \
    -o Artifacts/data_validation \
    python -c "from networksecurity.entity.config_entity import TrainingPipelineConfig, DataValidationConfig, DataIngestionConfig; from networksecurity.components.data_ingestion import DataIngestion; from networksecurity.components.data_validation import DataValidation; cfg=TrainingPipelineConfig(); di=DataIngestion(DataIngestionConfig(cfg)).initiate_data_ingestion(); DataValidation(di, DataValidationConfig(cfg)).initiate_data_validation();"


dvc stage add -n data_transformation \
    -d Artifacts/data_validation \
    -d networksecurity/components/data_transformation.py \
    -d networksecurity/entity/config_entity.py \
    -d networksecurity/constants/training_pipeline/__init__.py \
    -d networksecurity/utils/common.py \
    -o Artifacts/data_transformation \
    -o final_model/preprocessor.pkl \
    python -c "from networksecurity.entity.config_entity import TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig; from networksecurity.components.data_ingestion import DataIngestion; from networksecurity.components.data_validation import DataValidation; from networksecurity.components.data_transformation import DataTransformation; cfg=TrainingPipelineConfig(); di=DataIngestion(DataIngestionConfig(cfg)).initiate_data_ingestion(); dv=DataValidation(di, DataValidationConfig(cfg)).initiate_data_validation(); DataTransformation(dv, DataTransformationConfig(cfg)).initiate_data_transformation();"



dvc stage add -n model_trainer \
    -d Artifacts/data_transformation \
    -d networksecurity/components/model_trainer.py \
    -d networksecurity/entity/config_entity.py \
    -d networksecurity/constants/training_pipeline/__init__.py \
    -d networksecurity/utils/common.py \
    -d networksecurity/utils/ml_utils/model/estimator.py \
    -d networksecurity/utils/ml_utils/metric/classification_metric.py \
    -o Artifacts/model_trainer \
    -o final_model/model.pkl \
    python -c "from networksecurity.entity.config_entity import TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig; from networksecurity.components.data_ingestion import DataIngestion; from networksecurity.components.data_validation import DataValidation; from networksecurity.components.data_transformation import DataTransformation; from networksecurity.components.model_trainer import ModelTrainer; cfg=TrainingPipelineConfig(); di=DataIngestion(DataIngestionConfig(cfg)).initiate_data_ingestion(); dv=DataValidation(di, DataValidationConfig(cfg)).initiate_data_validation(); dt=DataTransformation(dv, DataTransformationConfig(cfg)).initiate_data_transformation(); ModelTrainer(dt, ModelTrainerConfig(cfg)).initiate_model_trainer();"

dvc remote s3 setup cmd from dagshub repo
dvc setup credentials cmd need to take it from dagshub repo

dvc pull -r origin

dvc push -r origin

then follow the git setps to push the current changes with dvc