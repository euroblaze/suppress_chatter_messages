# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HideMessageExtension(models.Model):
    _inherit = 'mail.message'

    hidden = fields.Boolean(default=False)

    def _is_hidden(self):
        for rec in self:
            return rec.hidden
