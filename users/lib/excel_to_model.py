# -*- coding: utf-8 -*-
import pandas
import logging

logger = logging.getLogger()


def excel_to_models(file_obj, model_serializer):
    """
    Accepts excel file, parses it as pandas dataframe and saves it as Django models
    :param file_obj:
    :param model_serializer:
    :return:
    """
    df = parse_excel(file_obj)
    num_ok, num_err = 0, 0
    for row in df.to_dict('records'):
        if row_to_model(row, model_serializer):
            num_ok += 1
        else:
            num_err +=1
    return num_ok, num_err


def parse_excel(file_obj):
    """Parse Excel file to pandas dataframe"""
    xl = pandas.ExcelFile(file_obj)
    df = xl.parse(0)  # first page
    return df


def row_to_model(row, model_serializer):
    """
    Save dataframe row to Django model
    :param row:
    :param model_serializer:
    :return:
    """
    logger.warning('row:'+str(row))
    serializer = model_serializer(data=row)
    if serializer.is_valid():
        logger.warning(serializer.validated_data)
        serializer.save()
        return True
    else:
        logger.warning(serializer.errors)
        return False
