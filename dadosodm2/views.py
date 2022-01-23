from django.shortcuts import render
from .models import Timeseriesresults, Timeseriesresultvalues, CvCensorcode, CvQualitycode, Units, Organizations
from django.utils import timezone
import pandas as pd
from django.utils import timezone
import datetime
import hidrocomp
from hidrocomp.series import Rainfall
import plotly.offline as pyo
import plotly.graph_objs as go
from functools import reduce
import hydro_api
from hydro_api.ana.hidro.serie_temporal import SerieTemporal
import matplotlib.pyplot as plt

datetime.datetime.now(tz=timezone.utc)


def paginainicial(request):
    context={}
    return render(request, 'index.html',context)

def projeto(request):
    context = {}

    return render(request,'dadosodm2/base.html',context)

def dados(request):

    dados = Flow(station='39970000', source='ANA')
    #df2 = Flow(station='39980000', source='ANA')

    result = Timeseriesresults.objects.get(pk=34789000)  # esse
    censor = CvCensorcode.objects.get(name='Unknown')
    quality = CvQualitycode.objects.get(name='Unknown')
    units_time = Units.objects.get(pk=1)
    time_inter = 1
    value_utc = 1
    source = Organizations.objects.get(pk=1)
    station = result.resultid.featureactionid.samplingfeatureid.samplingfeaturename

    time_serie_result_list = []

    for i in dados.index:
        obj_ts = Timeseriesresultvalues(resultid=result, censorcodecv=censor,
                                        qualitycodecv=quality, valuedatetimeutcoffset=value_utc,
                                        timeaggregationinterval=time_inter,
                                        timeaggregationintervalunitsid=units_time,
                                        valuedatetime=i.to_pydatetime(),
                                        datavalue=dados[dados.columns.values[0]][i])
        time_serie_result_list.append(obj_ts)
    Timeseriesresultvalues.objects.bulk_create(time_serie_result_list)


    return render(request,'dadosodm2/dados.html')
