import pandas as pd
import seaborn as sns
import numpy as np

while True:
    try:
        metric_log = pd.read_csv('./logs/metric_log.csv')
        hist_plot = sns.histplot(metric_log['absolute_error'], kde=True)
        # hist_plot.set(xlabel='absolute_error')
        fig = hist_plot.get_figure()
        fig.savefig('./logs/error_distribution.png')
        print('Файл успешно сохранен')
    except Exception as err:
        print(f'Возникла ошибка {type(err).__name__}: {err}')
