from __future__ import unicode_literals


class BaseEndpoint:
    base_url = '%s'

    def _url(self, endpoint, *args):
        return self.base_url % (endpoint % args)
