import pandas
import openpyxl
import configparser
import time
import os
import pdb
import shutil
import daily_kpi_analysis
import email_processing

def main_gui_func(subject, To, Message):
    start = time.time()
    print('Execution Starts!')
    time.sleep(1)
    config = configparser.ConfigParser()
    config.read(str(os.getcwd())+'\\config_dir\\config.ini')
    input_file_Daily_Counter_name = config.get('Data_Files', 'Input_Daily_Counter')
    input_Daily_Counter_file_path = str(os.getcwd())+'\\Input\\' + input_file_Daily_Counter_name

    print('Please Wait While Tool Complete its Execution!')
    time.sleep(2)
    daily_kpi_analysis.kpi_analysis_func(input_Daily_Counter_file_path)


    login_email = config.get('Data_Files', 'login_email')
    login_pw = config.get('Data_Files', 'login_pw')

    email_processing.email_func(login_email, login_pw, subject, To, Message)


    time.sleep(1)
    end = time.time()
    Execute_Time = "{:.3f}".format((end - start) / 60)
    print('The Execution Time of this Tool is %s minutes.' % Execute_Time)
    print('Tool Completed its Execution Successfully!')
    print('Thank You!')
    time.sleep(1)

    print('-----------------------------------------------')
    print('For Support: Danish Ali WX854280')
    print('Email: danish.ali3@huawei.com')
    print('Contact: 00971508552942')
    print('-----------------------------------------------')
    time.sleep(4)

    #ahsan.khan@huawei.com,fahad.izhar.siddiqui@huawei.com,mudassir.hussain4@huawei.com,haroon.waheed.butt@huawei.com,asifbukhari@huawei.com,Nabeel.Anwar@du.ae,abrar.mehmood.malik@huawei.com