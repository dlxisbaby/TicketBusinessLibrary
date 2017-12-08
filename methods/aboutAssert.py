#coding:utf-8

from robot.api import logger

from TicketBusinessLibrary import config

class Assert():
    def __init__(self):
        pass

    def _assert_two_result_one_by_one(self,expect,actual,msg=''):
        '''
        验证预期结果与实际结果是否相同\n
        :param expect: 预期结果\n
        :param actual: 实际结果\n
        '''
        if type(expect) == type(actual) == list or type(expect) == type(actual) == tuple:
            ex_leng = len(expect)
            ac_leng = len(actual)
            if ac_leng != ex_leng:
                raise AssertionError(u"预期与实际结果不同,结果长度不一致")
            for i in range(ex_leng):
                if expect[i] != actual[i]:
                    logger.info(u"预期结果为：{0}".format(expect[i]))
                    logger.info(u"实际结果为：{0}".format(actual[i]))
                    if msg == "":
                        raise AssertionError(u"预期与实际结果不同")
                    else:
                        raise AssertionError(msg)
                else:
                    continue
        else:
            self._assert_two_result2(expect,actual,msg)

    def _assert_two_result_as_string(self,expect,actual,msg=''):
        '''
        验证预期结果与实际结果是否相同\n
        :param expect: 预期结果\n
        :param actual: 实际结果\n
        '''
        if str(expect) == str(actual):
            logger.info(u"预期与实际结果相同")
        else:
            logger.info(u"预期结果为：{0}".format(expect))
            logger.info(u"实际结果为：{0}".format(actual))
            if msg == '':
                raise AssertionError(u"预期与实际结果不同")
            else:
                raise AssertionError(msg)

    def _assert_xml_resp_code(self,expect,actual,msg=''):
        '''
        验证预期结果与实际结果是否相同\n
        :param expect: 预期结果\n
        :param actual: 实际结果\n
        '''

        if expect == actual:
            logger.info(u"预期与实际状态相同")
        else:
            logger.info(u"预期状态为：{0}\"{1}\"".format(expect,config.resp_code[expect]))
            logger.info(u"实际状态为：{0}\"{1}\"".format(actual,config.resp_code[actual]))
            if msg == '':
                raise AssertionError(u"返回的状态与预期不相符")
            else:
                raise AssertionError(msg)

    def _assert_two_result2(self,expect,actual,msg=''):
        '''
        验证预期结果与实际结果是否相同\n
        :param expect: 预期结果\n
        :param actual: 实际结果\n
        '''

        if expect == actual:
            logger.info(u"预期与实际结果相同")
        else:
            logger.info(u"预期结果为：{0}".format(expect))
            logger.info(u"实际结果为：{0}".format(actual))
            if msg == '':
                raise AssertionError(u"预期与实际结果不同")
            else:
                raise AssertionError(msg)
