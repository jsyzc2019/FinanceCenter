# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from findy.database.schema.datatype import StockKdataCommon

wKdataBase = declarative_base()


class Stock1wkKdata(wKdataBase, StockKdataCommon):
    __tablename__ = 'stock_1wk_kdata'


class Stock1wkHfqKdata(wKdataBase, StockKdataCommon):
    __tablename__ = 'stock_1wk_hfq_kdata'


class Stock1wkBfqKdata(wKdataBase, StockKdataCommon):
    __tablename__ = 'stock_1wk_bfq_kdata'