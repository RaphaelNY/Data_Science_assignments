import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv("lab1_Coca_data.csv")

data['日期'] = pd.to_datetime(data['日期'])

data_week = data.groupby([pd.Grouper(freq='W', key='日期')]).agg({
    '收盘': 'mean'
})

data_month = data.groupby([pd.Grouper(freq='M', key='日期')]).agg({
    '收盘': 'mean'
})

def plot_chart(title, x, y, chart_type):
    plt.figure(figsize=(12, 6))
    plt.title(title)
    plt.xlabel('日期')
    plt.ylabel('平均收盘价')

    if chart_type == "line":
        plt.plot(x, y, label=title)
    elif chart_type == "scatter":
        plt.plot(x, y, 'o', label=title)
    elif chart_type == "bar":
        plt.bar(x, y, 4, label=title)

    plt.legend()
    plt.show()

plot_chart("周均值（折线图）", data_week.index, data_week['收盘'], "line")
plot_chart("月均值（折线图）", data_month.index, data_month['收盘'], "line")

plot_chart("周均值（散点图）", data_week.index, data_week['收盘'], "scatter")
plot_chart("月均值（散点图）", data_month.index, data_month['收盘'], "scatter")

plot_chart("周均值（柱形图）", data_week.index, data_week['收盘'], "bar")
plot_chart("月均值（柱形图）", data_month.index, data_month['收盘'], "bar")
