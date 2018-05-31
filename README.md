# Python-Number-Recognition
用 Python 客製化深度學習的過程，也可以自行繪製圖片進行結果預測

## 2018.06.01 修正中
此專案尚未修正完成

## 文字圖片產出範例
![0-2](https://github.com/telunyang/Python-Number-Recognition/blob/master/example01.png)
![5-5](https://github.com/telunyang/Python-Number-Recognition/blob/master/example02.png)
![5-7](https://github.com/telunyang/Python-Number-Recognition/blob/master/example03.png)
![7-9](https://github.com/telunyang/Python-Number-Recognition/blob/master/example04.png)

## 以 Windows 10 可用於繁體的字型為範例
![數字的label](https://github.com/telunyang/Python-Number-Recognition/blob/master/example05.png)

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
conda create -n tensorflow pip python=3.6
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
```
set "KERAS_BACKEND=tensorflow"
```

## 說明
1. word.txt

預測文字的來源，目前以數字為主 (0,1,2,3,4,5,6,7,8,9)。


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

字型庫，用來匯出同個數字、不同字型的圖片結果，建議購買字型工具，並尋找合適的字型檔案來使用，若無置設，請自行新增。


8. words/

執行 gen.py 後，其產生的圖片放置處，若無置設，請自行新增。


9. test/

放置上傳圖片與轉成 csv 檔的放置地點，若無置設，請自行新增。

切記：執行完 gen.py 與 train.py 後，要在裡面放自行繪製的 0 ~ 9.png 圖片，28 x 28 像素，可以小畫家中用 Ctrl 加上滾輪來放大編輯。


10. model.config

訓練後的模型設定。


11. model.weight

權重。