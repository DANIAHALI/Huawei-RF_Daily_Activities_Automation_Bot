import pandas
import openpyxl
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from openpyxl.styles.borders import Border, Side
from openpyxl import load_workbook
from openpyxl.chart import BarChart3D, Reference, AreaChart, AreaChart3D, Series, LineChart, LineChart3D
import os
import pdb
import graphs_formation
from openpyxl.styles import NamedStyle, Font, Border, Side
import excel2img

def kpi_analysis_func(input_file):
    print('Processing KPIs!')

    inputdailydf = pandas.read_excel(input_file, sheet_name= 'Subreport 1')
    outputdailydf = pandas.DataFrame()

    # KPIs Calculation
    outputdailydf['Date'] = inputdailydf['Date']
    outputdailydf['User Downlink Average Throughput(Gbps)'] = ((inputdailydf['N.ThpVol.DL(kbit)'] - inputdailydf['N.ThpVol.DL.LastSlot(kbit)']) / inputdailydf['N.ThpTime.DL.RmvLastSlot(microsecond)'])
    outputdailydf['User Uplink Average Throughput(Gbps)'] = ((inputdailydf['N.ThpVol.UL(kbit)'] - inputdailydf['N.ThpVol.UE.UL.SmallPkt(kbit)']) / inputdailydf['N.ThpTime.UE.UL.RmvSmallPkt'])
    outputdailydf['Cell Downlink Average Throughput(Gbps)'] = (inputdailydf['N.ThpVol.DL.Cell(kbit)'] / inputdailydf['N.ThpTime.DL.Cell(microsecond)'])
    outputdailydf['Cell Uplink Average Throughput(Gbps)'] = (inputdailydf['N.ThpVol.UL.Cell(kbit)'] / inputdailydf['N.ThpTime.UL.Cell(microsecond)'])
    outputdailydf['Downlink Resource Block Utilizing Rate'] = (inputdailydf['N.PRB.DL.Used.Avg'] / inputdailydf['N.PRB.DL.Avail.Avg'])*100
    outputdailydf['Uplink Resource Block Utilizing Rate'] = (inputdailydf['N.PRB.UL.Used.Avg'] / inputdailydf['N.PRB.UL.Avail.Avg'])*100
    outputdailydf['Radio Network Unavailability Rate'] = inputdailydf['NR Radio Network Availability Rate(%)']
    outputdailydf['Downlink Traffic Volume(GB)'] = inputdailydf['N.ThpVol.DL(kbit)']/8000000
    outputdailydf['Uplink Traffic Volume(GB)'] = inputdailydf['N.ThpVol.UL(kbit)']/8000000
    outputdailydf['Average User Number'] = inputdailydf['N.User.NsaDc.PSCell.Avg']
    outputdailydf['Maximum User Number'] = inputdailydf['N.User.RRCConn.Max']
    outputdailydf['SgNB Addition Success Rate'] = (inputdailydf['N.NsaDc.SgNB.Add.Succ'] / inputdailydf['N.NsaDc.SgNB.Add.Att']) * 100
    outputdailydf['Intra-SgNB PSCell Change Success Rate'] = (inputdailydf['N.NsaDc.IntraSgNB.PSCell.Change.Succ'] / inputdailydf['N.NsaDc.IntraSgNB.PSCell.Change.Att']) * 100
    outputdailydf['Inter-SgNB PSCell Change Success Rate'] = (inputdailydf['N.NsaDc.InterSgNB.PSCell.Change.Succ'] / inputdailydf['N.NsaDc.InterSgNB.PSCell.Change.Att']) * 100
    outputdailydf['SgNB-Triggered Abnormal SgNB Release Rate'] = (inputdailydf['N.NsaDc.SgNB.AbnormRel'] / inputdailydf['N.NsaDc.SgNB.Rel']) * 100
    outputdailydf['Network availability Rate (System)'] = inputdailydf['Cell Availability Rate -sys(%)']

    header_list = list(outputdailydf.columns.values)
    pdb.set_trace()
    header_list.pop(0)


    for i in range(len(header_list)):

        graphs_formation.pivot_attr(outputdailydf, header_list[i])

    writer = pandas.ExcelWriter(str(os.getcwd()) + '\\Output\\output.xlsx')
    outputdailydf.to_excel(writer, 'Daily KPIs Analysis', index=False)
    writer.save()
    writer.close()
