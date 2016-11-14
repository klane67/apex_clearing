from __future__ import unicode_literals

from dateutil.parser import parse

from . import AchRelationshipApprovalMethod
from .enums import AchRelationshipStatus, BankAccountType
from ...atlas.accounts import ApexAccount
from ...structs import DictStruct

__all__ = [
    'AchRelationshipCancellationState',
    'AchRelationshipApprovalState',
    'AchRelationshipRequest',
    'AchRelationshipResponseStructV2',
]


class AchRelationshipCancellationState(DictStruct):
    """
    reason: Reason why the ACH relationship was cancelled
    comment: Additional comment explaining why the ACH relationship was canceled
    cancellationTime: Date/time the ACH relationship was cancelled
    cancelledBy:
    """
    fields = ['reason', 'comment', 'cancellationTime', 'cancelledBy']


class AchRelationshipApprovalState(DictStruct):
    """
    approvalTime: Time the ACH relationship was approved
    approvedBy:
    """
    fields = ['approvalTime', 'approvedBy']


class AchRelationshipRequest(DictStruct):
    """
    account (string): Apex account for this relationship
    bankRoutingNumber (string): routing number for the target bank US Bank routing number is composed of 9 digits
    bankAccount (string): account number of the target bank account ACH supports bank account number of max length 17
    bankAccountOwnerName (string): name of the person listed as the bank account owner
    bankAccountType (string): type of the target bank account
    nickname (string): nickname for this ACH relationship (e.g. "My Checking Account")
    approvalMethod (string): method that will be used to approve this relationship
    """
    fields = {
        'account': (None, True),
        'bankRoutingNumber': (None, True),
        'bankAccount': (None, True),
        'bankAccountOwnerName': (None, True),
        'bankAccountType': (BankAccountType, True),
        'nickname': (None, True),
        'approvalMethod': (AchRelationshipApprovalMethod, True),
    }


class AchRelationshipResponseStructV2(DictStruct):
    """
    id: (optional) Unique identifier of this relationship
    account: (optional) Apex account ID
    bankRoutingNumber: (optional) Routing number for the bank where the bank account resides
    bankAccount: (optional) Bank account number (obscured)
    bankAccountOwnerName: (optional) Name of the person listed as the bank account owner
    bankAccountType: (optional) Type of bank account
    nickname: (optional) Nickname for this ACH relationship (e.g. "My Checking Account")
    approvalMethod: (optional) Method that will be used to approve this relationship
    creationTime: (optional) Date/time this relationship was created
    status: (optional) Current status of this relationship
    approval: (optional)
    cancellation: (optional)
    """
    fields = {
        'id': None,
        'account': (ApexAccount,),
        'bankRoutingNumber': None,
        'bankAccount': None,
        'bankAccountOwnerName': None,
        'bankAccountType': None,
        'nickname': None,
        'approvalMethod': (AchRelationshipApprovalMethod,),
        'creationTime': (parse,),
        'status': (AchRelationshipStatus,),
        'approval': (AchRelationshipApprovalState,),
        'cancellation': (AchRelationshipCancellationState,),
    }
