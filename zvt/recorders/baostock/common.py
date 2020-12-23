# -*- coding: utf-8 -*-
from zvt.contract import IntervalLevel
from zvt.contract.common import EntityType
from zvt.domain import ReportPeriod


def to_bao_trading_level(trading_level: IntervalLevel):

    if trading_level == IntervalLevel.LEVEL_5MIN:
        return '5'
    if trading_level == IntervalLevel.LEVEL_15MIN:
        return '15'
    if trading_level == IntervalLevel.LEVEL_30MIN:
        return '30'
    if trading_level == IntervalLevel.LEVEL_1HOUR:
        return '60'
    if trading_level == IntervalLevel.LEVEL_1DAY:
        return 'd'
    if trading_level == IntervalLevel.LEVEL_1WEEK:
        return 'w'
    if trading_level == IntervalLevel.LEVEL_1MON:
        return 'm'

    raise Exception("trading level not support {}".format(trading_level))


def to_bao_trading_field(trading_level):
    if trading_level == 'd':
        return "date, open, high, low, close, preclose, volume, amount, adjustflag, turn, tradestatus, pctChg, peTTM, psTTM, pcfNcfTTM, pbMRQ, isST"
    if trading_level == 'w' or trading_level == 'm':
        return "date, open, high, low, close, volume, amount, adjustflag, turn, pctChg"
    else:
        return "date, time, open, high, low, close, volume, amount, adjustflag"


def to_bao_entity_id(security_item):
    if security_item.entity_type == EntityType.Stock.value or security_item.entity_type == EntityType.Index.value:
        if security_item.exchange == 'sh':
            return 'sh.{}'.format(security_item.code)
        if security_item.exchange == 'sz':
            return 'sz.{}'.format(security_item.code)