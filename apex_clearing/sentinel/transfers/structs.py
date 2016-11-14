from __future__ import unicode_literals

from dateutil.parser import parse

from .enums import IraContributorType, IraDistributionReason, \
    IraTaxWithholdingType, TransferDirection, TransferDisbursementType, \
    TransferMechanism, TransferRejectReason, TransferState
from ...structs import DictStruct

__all__ = [
    'TransferSummaryStruct',
    'FeeStruct',
    'IraContributionStruct',
    'AchDepositResponse',
    'AchDepositRequest',
    'AchWithdrawalRequest',
    'AchWithdrawalResponse',
    'IraDistributionStruct',
    'TaxWithholdingStruct',
    'TransferResponse',
]


class TransferSummaryStruct(DictStruct):
    """
    transferTime (string, optional)
    transferId (string, optional)
    mechanism (string, optional)
    direction (string, optional)
    state (string, optional)
    rejectReason (string, optional)
    requestedAmount (number, optional),
    amount (number, optional),
    fees (Array[FeeStruct], optional)
    """
    fields = {
        'transferTime': (parse,),
        'transferId': (None,),
        'mechanism': (TransferMechanism,),
        'direction': (TransferDirection,),
        'state': (TransferState,),
        'rejectReason': (TransferRejectReason,),
        'requestedAmount': (None,),
        'amount': (None,),
        'fees': ([FeeStruct],),
    }


class FeeStruct(DictStruct):
    """
    type: Type of fee
    customerDebitAmount: Amount being debited from the customer for this fee
    firmCreditAmount: Amount being credited to the firm for this fee
    correspondentNetAmount: Amount being credited or debited to the correspondent for this fee.
                            This will vary depending on the correspondent's configuration for this particular fee. If a correspondent is adding their own premium to a fee, this value will be positive and represents a net credit to the correspondent which is the premium being collected for this fee. If a correspondent is covering a fee, this value will be negative and represents a debit from the correspondent to cover that fee on behalf of the customer.
    """
    fields = [
        'type',
        'customerDebitAmount',
        'firmCreditAmount',
        'correspondentNetAmount',
    ]


class IraContributionStruct(DictStruct):
    """
    contributionType: contributionType (string): type of retirement account contribution being made
    contributionYear: year to apply retirement account contribution to
    """
    fields = {
        'contributionType': (IraContributorType, True),
        'contributionYear': None,
    }


class AchDepositResponse(DictStruct):
    """
    The submitted information will be validated and then evaluated. Once 
    a transfer is evaluated the status of the transfer will be returned to 
    the submitter. Transfers submitted after the daily cutoff will not be 
    evaluated until the following day.
    
    transferId: identifier generated to uniquely identify a transfer
    externalTransferId: external identifier supplied by the submitter
    mechanism: mechanism used to perform the transfer
    direction: directionality of the transfer
    state: workflow state that the transfer is currently in
    rejectReason: reason the transfer is rejected
    amount: amount being deposited into the customers brokerage account
    estimatedFundsAvailableDate: estimated date that the funds will be available for trading
    achRelationshipId: id of the ACH relationship
    fees: fees being charged for this transfer
    iraDetails:
    """
    fields = {
        'transferId': (None, True),
        'mechanism': (TransferMechanism, True),
        'direction': (TransferDirection, True),
        'state': (TransferState, True),
        'amount': (None, True),
        'estimatedFundsAvailableDate': (parse, True),
        'achRelationshipId': (None, True),
        'fees': ([FeeStruct], True),
        'externalTransferId': None,
        'rejectReason': (TransferRejectReason,),
        'iraDetails': (IraContributionStruct,),
    }


class AchDepositRequest(DictStruct):
    """
    externalTransferId: external identifier supplied by the submitter
    amount: amount being transferred
    achRelationshipId: id of the ach relationship
    daysToHoldFunds: number of days to hold funds in a suspected date; defaults to 0
    iraDetails:
    """
    fields = {
        'externalTransferId': (None, True),
        'amount': (None, True),
        'achRelationshipId': (None, True),
        'daysToHoldFunds': None,
        'iraDetails': (IraContributionStruct,),
    }


class AchWithdrawalRequest(DictStruct):
    """
    externalTransferId (string): external identifier supplied by the submitter ,
    disbursementType (string): type of disbursement / withdrawal being performed = ['PARTIAL_BALANCE', 'FULL_BALANCE'],
    amount (number, optional): amount to withdraw, should be left blank for full balance transfers ,
    achRelationshipId (string): details describing the accounts involved in this ACH transfer ,
    iraDetails (IraDistributionStruct, optional)
    """
    fields = {
        'externalTransferId': (None, True),
        'disbursementType': (TransferDisbursementType, True),
        'amount': None,
        'achRelationshipId': (None, True),
        'iraDetails': (IraDistributionStruct,),
    }


class AchWithdrawalResponse(DictStruct):
    """
    transferId (string): identifier generated to uniquely identify a transfer
    externalTransferId (string, optional): external identifier supplied by the submitter
    mechanism (string): mechanism used to perform the transfer
    direction (string): directionality of the transfer
    state (string): workflow state that the transfer is currently in
    rejectReason (string, optional): reason the transfer is rejected
    disbursementType (string): type of disbursement / withdrawal being performed,
    requestedAmount (number, optional): the amount specified in the original request ,
    amount (number, optional): the amount that will actually be deposited into the customers bank account. ,
    achRelationshipId (string): id of the ACH relationship ,
    iraDetails (IraDistributionStruct, optional),
    fees (Array[FeeStruct]): fees being charged for this transfer
    """
    fields = {
        'transferId': (None, True),
        'externalTransferId': None,
        'mechanism': (TransferMechanism, True),
        'direction': (TransferDirection, True),
        'state': (TransferState, True),
        'rejectReason': (TransferRejectReason,),
        'disbursementType': (TransferDisbursementType, True),
        'requestedAmount': None,
        'amount': None,
        'achRelationshipId': (None, True),
        'iraDetails': (IraDistributionStruct,),
        'fees': ([FeeStruct], True),
    }


class IraDistributionStruct(DictStruct):
    """
    distributionReason (string): Reason that funds are being distributed from an IRA account,
    federalTaxWithholding (TaxWithholdingStruct, optional),
    stateTaxWithholding (TaxWithholdingStruct, optional),
    receivingInstitutionName (string, optional): Name of the financial institution receiving transferred retirement account funds. This is only required when transferring to an identical retirement account at another financial institution.
    """
    fields = {
        'distributionReason': (IraDistributionReason, True),
        'federalTaxWithholding': (TaxWithholdingStruct, None),
        'stateTaxWithholding': (TaxWithholdingStruct, None),
        'receivingInstitutionName': None,
    }


class TaxWithholdingStruct(DictStruct):
    """
    valueType (string): Type of withholding value
    value (number): Amount to withhold
    """
    fields = {
        'valueType': (IraTaxWithholdingType, True),
        'value': (None, True),
    }


class TransferResponse(DictStruct):
    """
    transferId (string): identifier generated to uniquely identify a transfer
    externalTransferId (string, optional): external identifier supplied by the submitter
    mechanism (string): mechanism used to perform the transfer
    direction (string): directionality of the transfer
    state (string): workflow state that the transfer is currently in
    rejectReason (string, optional): reason the transfer is rejected
    """
    fields = {
        'transferId': (None, True),
        'externalTransferId': None,
        'mechanism': (TransferMechanism, True),
        'direction': (TransferDirection, True),
        'state': (TransferState, True),
        'rejectReason': (TransferRejectReason,),
    }
