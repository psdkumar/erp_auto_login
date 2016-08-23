#!/usr/bin/env python

import erp

obj = erp.AutoLoginERP()
obj.openERP().enterDetails().login().mails()