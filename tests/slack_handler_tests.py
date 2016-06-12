"""
Tests for slack_handler module

To run the tests, add a slack hook url to HOOK_URL
"""
# pylint: disable=missing-docstring, import-error, wildcard-import
# pylint: disable=attribute-defined-outside-init,unused-wildcard-import, no-init
import logging
import json

from nose.tools import *

from slack_handler.slack_handler import (
    SlackHandler, color_picker, build_logger
    )


HOOK_URL = ''

logger = logging.getLogger("Slack Logging Test")
handler = SlackHandler(HOOK_URL)
fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handler.setFormatter(logging.Formatter(fmt))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class TestSlackHandler(object):
    def setup(self):
        print('SETUP!')
        self.logger = logger
        self.handler = handler

    def teardown(self):
        print('TEAR DOWN!')
        #self.handler._clear_buffer()
        self.handler.close()

    @raises(ValueError)
    def test_hook_url(self):
        new_handler = SlackHandler('http://www.google.com')

    def test_clear_buffer(self):
        eq_(self.handler.buffer, [])
        eq_(self.handler.payload, {})
        eq_(self.handler.json, "")

        self.logger.debug("Test log data should be deleted.")
        ok_(self.handler.buffer)

        self.handler._clear_buffer()
        eq_(self.handler.buffer, [])

    def test_format_buffer_truth(self):
        assert not self.handler.format_buffer()
        self.logger.debug('Handler now has a buffer entry.')
        assert self.handler.format_buffer()

    def test_format_buffer(self):
        # test that msg_string is formatted as json
        self.logger.info('Test buffer formatting.')
        self.handler.format_buffer()
        try:
            j = json.loads(self.handler.json)
        except Exception:
            self.handler._clear_buffer()
            raise
        else:
            ok_(j)
        finally:
            self.handler._clear_buffer()

    def test_format_buffer_empty(self):
        assert not self.handler.format_buffer()

    def test_basic(self):
        self.logger.debug("This is a basic test of the slack logging module.")
        response = self.handler.flush()
        eq_(response.status_code, 200)

    def test_multiline(self):
        eq_(self.handler.buffer, [])
        self.logger.debug('This is a test of of multi-line slack logging.')
        for x in range(10):
            self.logger.debug('Test %d' % x)
        response = self.handler.flush()
        eq_(response.status_code, 200)
        self.handler._clear_buffer()
        eq_(self.handler.buffer, [])

    def test_empty(self):
        response = self.handler.flush()
        assert not response

    @nottest
    def buffer_name(self):
        self.logger.debug('Please provide log record info.')
        for record in self.handler.buffer:
            print(record)
            print(record.msg % getattr(record, "args"))
            print(dir(record))
            for attr in dir(record):
                print(attr)
                try:
                    print('%s: %s' % (attr, getattr(record, attr)))
                except Exception:
                    pass

        self.handler.buffer = []
        raise Exception

    def test_color_picker_danger(self):
        # should return a color repping the highest value
        levels = ['ERROR', 'WARNING', 'INFO', 'DEBUG']
        eq_(color_picker(levels)[1], 'danger')

    def test_color_picker_warn(self):
        levels = ['WARNING', 'INFO', 'DEBUG']
        eq_(color_picker(levels)[1], 'warning')

    def test_color_picker_good(self):
        levels = ['INFO', 'DEBUG']
        eq_(color_picker(levels)[1], 'good')

    def test_color_picker_unknown(self):
        eq_(color_picker(['weird'])[1], 'good')

    def test_warning(self):
        self.logger.info('This is a warning.')
        self.logger.warning('Watch out for Godzilla.')
        response = self.handler.flush()
        assert 'warning' in response.request.body

    def test_error(self):
        self.logger.info('This will be an error message!')
        self.logger.error('Oh no GODZILLA!')
        self.logger.error("HE'S ATTACKING THE CITY!")
        response = self.handler.flush()
        assert 'danger' in response.request.body

    def test_build_logger(self):
        # tests the build_logger convenience function
        logger = build_logger(base_url)
        ok_(logger)

    def test_lazy_join(self):
        self.logger.info('We also need to test:  %s', 'lazy argument parsing!')
        response = self.handler.flush()
        ok_(response)
