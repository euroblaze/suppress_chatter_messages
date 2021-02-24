# -*- coding: utf-8 -*-
# from odoo import http


# class OmSuppressChatterMessages(http.Controller):
#     @http.route('/om_suppress_chatter_messages/om_suppress_chatter_messages/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_suppress_chatter_messages/om_suppress_chatter_messages/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_suppress_chatter_messages.listing', {
#             'root': '/om_suppress_chatter_messages/om_suppress_chatter_messages',
#             'objects': http.request.env['om_suppress_chatter_messages.om_suppress_chatter_messages'].search([]),
#         })

#     @http.route('/om_suppress_chatter_messages/om_suppress_chatter_messages/objects/<model("om_suppress_chatter_messages.om_suppress_chatter_messages"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_suppress_chatter_messages.object', {
#             'object': obj
#         })
