# Python-Number-Recognition
用 Python 客製化深度學習的過程，也可以自行繪製圖片進行結果預測

## 製作流程
1. 安裝 Anaconda
[下載頁面](https://www.anaconda.com/download/)
註: 有分 3.6 與 2.7 版本，也有分 64 與 32 位元，請依需求下載。

安裝結束後，請進入 Anaconda Rrompt

2. 建立你的專案資料夾，之後要在裡面進行環境安裝與設定
```
mkdir <your-project-path>
cd <your-project-path>
```

3. 建立 Conda 環境，這裡安裝 Python 3.6，環境名稱為 tensorflow
```
C:> conda create -n tensorflow pip python=3.6
```

4. 啟動 Conda 環境
```
activate tensorflow
```
之後環境會從 (base) 變成 (tensorflow)


5. 安裝 TensorFlow
註: 先進 Anaconda Prompt

僅有 CPU 的條件下，進行下列安裝
```
conda install -c conda-forge tensorflow 
```

6. 安裝 Keras
```
conda install -c conda-forge keras
```

7. 安裝 pygame
```
pip install pygame
```

8. 安裝 scikit-learn
```
conda install -c anaconda scikit-learn
```

9. 安裝 PIL
```
pip install pillow
```

10. 安裝 matplotlib
```
conda install -c conda-forge matplotlib
```

## 設定 KERAS_BACKEND=tensorflow
set "KERAS_BACKEND=tensorflow"

## 說明
1. word.txt
預測文字的來源，目前以數字為主。

2. gen.py
產生訓練用的數字圖片。

3. train.py
建立深度學習的模型，並將訓練結果加以儲存，以便之後的預測。

4. test.py
進行預測，並取得比對後的結果。

5. index.html
上傳用的頁面。

6. prediction.php
預測結果的展示頁面。

7. ttf/
字型庫，用來匯出同個數字、不同字型的圖片結果。教學用途，若有侵權，敬請告知，將在 24 小時內刪除。

8. words/
執行 gen.py 後，其產生的圖片放置處。

9. test/
放置上傳圖片與轉成 csv 檔的放置地點。

10. model.config
訓練後的模型設定。

11. model.weight
權重。