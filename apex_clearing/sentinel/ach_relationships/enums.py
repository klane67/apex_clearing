from __future__ import unicode_literals

from enum import Enum

__all__ = [
    'AchRelationshipApprovalMethod',
    'BankAccountType',
    'AchRelationshipStatus'
]


class AchRelationshipApprovalMethod(Enum):
    MicroDeposit = 'MICRO_DEPOSIT'
    Yodlee = 'YODLEE'
    Plaid = 'PLAID'
    Giact = 'GIACT'
    Apex = 'APEX'
    VoidedCheck = 'VOIDED_CHECK'


class BankAccountType(Enum):
    Checking = 'CHECKING'
    Savings = 'SAVINGS'


class AchRelationshipStatus(Enum):
    Pending = 'PENDING'
    Canceled = 'CANCELED'
    Approved = 'APPROVED'
