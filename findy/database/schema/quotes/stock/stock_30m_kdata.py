# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from findy.database.schema.datatype import StockKdataCommon

tmKdataBase = declarative_base()


class Stock30mKdata(tmKdataBase, StockKdataCommon):
    __tablename__ = 'stock_30m_kdata'


class Stock30mHfqKdata(tmKdataBase, StockKdataCommon):
    __tablename__ = 'stock_30m_hfq_kdata'


class Stock30mBfqKdata(tmKdataBase, StockKdataCommon):
    __tablename__ = 'stock_30m_bfq_kdata'
