# 輔仁大學美食餐廳整合系統

### 版本架構
版本：0.1
```
fju_foodmap/                      # 專案根目錄
├── fju_foodmap/                  # 專案設定目錄
│   ├── __init__.py
│   ├── settings.py              # 專案設定檔
│   ├── urls.py                  # 主要 URL 配置
│   ├── asgi.py                  # ASGI 配置
│   └── wsgi.py                  # WSGI 配置
│
├── index/                        # 主要應用程式
│   ├── migrations/              # 資料庫遷移檔案
│   ├── static/                  # 靜態檔案
│   │   └── index/
│   │       ├── css/
│   │       │   └── style.css    # 樣式表
│   │       ├── js/
│   │       │   └── main.js      # JavaScript
│   │       └── images/          # 圖片資源
│   │           ├── campus-food.jpg
│   │           ├── nearby-food.jpg
│   │           └── popular-food.jpg
│   │
│   ├── templates/               # 模板目錄
│   │   └── index/
│   │       ├── base.html        # 基礎模板
│   │       └── index.html       # 首頁模板
│   │
│   ├── __init__.py
│   ├── admin.py                 # 管理介面設定
│   ├── apps.py                  # 應用程式設定
│   ├── models.py               # 資料模型
│   ├── views.py                # 視圖函數
│   ├── urls.py                 # URL 路由
│   └── tests.py                # 測試檔案
│
├── manage.py                    # Django 管理工具
└── requirements.txt            # 專案依賴套件
```
---
### 版本內容:
```
新增前端:
  模板：
    1. 首頁
    2. 基礎
    3.

  靜態檔案:
    1. css
    2. JS
```
  
