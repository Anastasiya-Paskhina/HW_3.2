import csv

from django.shortcuts import render
from django.views.generic import TemplateView


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        with open('inflation_russia.csv', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            rows_list = list()
            for row in reader:
                row_list = list()
                for item in row:
                    if item:
                        row_list.append(item)
                    else:
                        row_list.append('-')
                rows_list.append(row_list)
            table_head = rows_list[0]
            rows_list = rows_list[1:]
            context = {'head': table_head,
                       'table': rows_list}
            return render(request, self.template_name,
                          context)

