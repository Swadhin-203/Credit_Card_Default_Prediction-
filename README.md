# **End to end CreditCardFraud1 Detection Project**

How to run the project:
1. Create a new conda environment with the following command:

```
conda create -p venv python==3.9.17 -y
```

2. Activate the conda environment with the following command:
```
conda activate venv/
```

3. Install the package requirements:
```
pip install -r requirements.txt
```

4. Run the training pipeline to train the model and create the artifacts:
```
python src\pipelines\training_pipeline.py
```

5. Mlflow ui can be accessed by running: (Optional)
```
mlflow ui
```

<!-- 6. Run:
```
python app.py ## initiates flask application
```

7. Go to:
```
home page: 120.0.0.1:5000/   ## home page
submit page: 120.0.0.1:5000/submit  ## prediction page

``` -->