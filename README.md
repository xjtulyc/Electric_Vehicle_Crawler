# Electric Vehicle Crawler | 新能源汽车爬虫

## 关于项目

[项目背景](https://github.com/xjtulyc/Electric_Vehicle_Crawler/blob/main/docs/background.md)

[API](https://github.com/xjtulyc/Electric_Vehicle_Crawler/blob/main/docs/api.md)

## 运行

下载项目到本地

```
git clone git@github.com:xjtulyc/Electric_Vehicle_Crawler.git
```

爬取数据，依次爬取汽车销量等需要分析的数据。

```shell
python scraler.py
```

使用线性回归和灰色预测对数据进行分析，其中充电桩的空间分布使用聚类分析进行度量。

```shell
python analysis.py
```
## 依赖

```requirements.txt
numpy
pandas
selenium
bs4
```

## 项目进展

### 1. 数据爬虫 （2023-01-10 to 2023-01-25）

#### 1.1. 汽车销量 （2023-01-10 to 2023-01-14）

#### 1.2. 汽车配置水平 （2023-01-14 to 2023-01-16）

#### 1.3. 汽油柴油价格 （2023-01-16 to 2023-01-20）

#### 1.4. 充电桩数目和空间分布 （2023-01-20 to 2023-01-25）

### 2. 数据分析 （2023-01-26 to 2023-02-05）

#### 2.1. 线性回归 （2023-01-26 to 2023-02-01）

#### 2.2. 灰色预测 （2023-02-02 to 2023-02-05）
