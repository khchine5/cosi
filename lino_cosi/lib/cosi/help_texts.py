# -*- coding: UTF-8 -*-
# generated by lino.sphinxcontrib.help_text_builder
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
help_texts = {
    'lino_cosi.lib.b2c.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_cosi.lib.b2c.Plugin.import_statements_path' : _("""A path wildcard pointing to xml files which need to get imported."""),
    'lino_cosi.lib.b2c.Plugin.delete_imported_xml_files' : _("""This attribute define whether, Cosi have to delete the SEPA file
after it get imported."""),
    'lino_cosi.lib.b2c.camt.BankTransaction' : _("""Single transaction that is part of a bank statement."""),
    'lino_cosi.lib.b2c.camt.BankStatement' : _("""A bank statement groups data about several bank transactions."""),
    'lino_cosi.lib.b2c.camt.CamtParser' : _("""Parser for camt bank statement import files."""),
    'lino_cosi.lib.b2c.models.ImportStatements' : _("""Import the .xml files found in the directory specified at
import_statements_path."""),
    'lino_cosi.lib.b2c.models.Account' : _("""A bank account related to a given Partner."""),
    'lino_cosi.lib.b2c.models.Account.account_name' : _("""Name of the account, as assigned by the account servicing
institution, in agreement with the account owner in order to
provide an additional means of identification of the account.
Usage: The account name is different from the
owner_name. The account name is used in certain user
communities to provide a means of identifying the account, in
addition to the account owner’s identity and the account
number."""),
    'lino_cosi.lib.b2c.models.Account.owner_name' : _("""Name by which a party is known and which is usually used to
identify that party."""),
    'lino_cosi.lib.b2c.models.Statement' : _("""A bank statement."""),
    'lino_cosi.lib.b2c.models.Statement.sequence_number' : _("""The legal sequential number of the statement, as assigned by
the bank."""),
    'lino_cosi.lib.b2c.models.Transaction' : _("""A transaction within a bank statement."""),
    'lino_cosi.lib.b2c.models.Transaction.transfer_type' : _("""The actual historic name of the txcd."""),
    'lino_cosi.lib.b2c.models.Transaction.txcd' : _("""The Bank Transaction Code (<BkTxCd>) or “transfer type”.
Actually it is the “proprietary” part of this code."""),
    'lino_cosi.lib.b2c.models.Transaction.txcd_issuer' : _("""The issuer or the txcd."""),
    'lino_cosi.lib.b2c.models.Transaction.txcd_text' : _("""Virtual field with the textual translated description of the
txcd.  Currently this works only for Belgian codes
where txcd_issuer is “BBA” as defined in
lino_cosi.lib.b2c.febelfin)."""),
    'lino_cosi.lib.contacts.models.Partner' : _("""An version of lino_xl.lib.contacts.models.Partner which
adds accounting fucntionality."""),
    'lino_cosi.lib.contacts.models.Person' : _("""An version of lino_xl.lib.contacts.models.Person which
adds accounting fucntionality."""),
    'lino_cosi.lib.contacts.models.Company' : _("""An version of lino_xl.lib.contacts.models.Company which
adds accounting fucntionality."""),
    'lino_cosi.lib.delivery.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_cosi.lib.delivery.models.ShippingMode' : _("""Represents a possible method of how the items described in a
SalesDocument are to be transferred from us to our customer."""),
    'lino_cosi.lib.orders.Plugin' : _("""See lino.core.plugin.Plugin."""),
}
