# 💳 **CreditCardFraud Detection Project** 🛡️

😉How to run the project:
1. Create a new conda environment with the following command:

```bash
conda create -p venv python==3.9.18 -y
```

2.😊 Activate the conda environment with the following command:
```bash
conda activate venv/
```

3.✌️ Install the package requirements:
```bash
pip install -r requirements.txt
```
4. 😎Export the following parameters

```bash
export MLFLOW_TRACKING_USERNAME=tejas05in
```
```bash
export MLFLOW_TRACKING_PASSWORD=9efcb5c7b79d0e949378459b922b1462a80fa413
```

5. 😁Run the training pipeline to train the model and create the artifacts:
```bash
python src/pipelines/training_pipeline.py
```

6.🤗 Mlflow ui can be accessed by running: (Optional)
```bash
mlflow ui
```

7.🙌 Run:
```bash
streamlit run application.py ## initiates streamlit application
```

8.🤩🥳 Upload data:
```
Upload csv file to get the results
```

#### 🌟Mlflow tracking with dagshub:

```angular2html
MLFLOW_TRACKING_URI=https://dagshub.com/Swadhin-203/Credit_Card_Default_Prediction-.mlflow
```
### 🚀Project Demo Video 🎥 [Click Here To Watch](https://www.youtube.com/watch?v=SAAXYqVyyDg)



#### Docker image
```docker
docker pull tejas05in/ccfapp
```
## Contributors 🚀

A big thank you to all the wonderful people who have contributed to this project! 🙌

- [Swadhin Gyanajyoti Nayak🌟](https://github.com/Swadhin-203)
- [Tejas J 🤗](https://github.com/tejas05in)
- [Nihal Barhaiyya🎉](https://github.com/Nihal434)
- [Maurya Mayank🤩](https://github.com/mmayank2)
