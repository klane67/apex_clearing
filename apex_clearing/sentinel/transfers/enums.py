from __future__ import unicode_literals

from enum import Enum


__all__ = [
    'TransferMechanism',
    'TransferDirection',
    'TransferState',
    'TransferRejectReason',
    'TransferDisbursementType',
    'IraContributorType',
    'IraDistributionReason',
    'IraTaxWithholdingType',
]

class TransferMechanism(Enum):
    Wire = 'WIRE'
    Ach = 'ACH'
    Check = 'CHECK'
    CashJournal = 'CASH_JOURNAL'
    DebitCard = 'DEBIT_CARD'
    AutoPost = 'AUTO_POST'


class TransferDirection(Enum):
    Incoming = 'INCOMING'
    Outgoing = 'OUTGOING'


class TransferState(Enum):
    Canceled = 'CANCELED'
    Rejected = 'REJECTED'
    PendingBrokerApproval = 'PENDING_BROKER_APPROVAL'
    Pending = 'PENDING'
    Frozen = 'FROZEN'
    Approved = 'APPROVED'
    FundsPosted = 'FUNDS_POSTED'
    SentToBank = 'SENT_TO_BANK'
    FailedAtBank = 'FAILED_AT_BANK'
    CompleteRestricted = 'COMPLETE_RESTRICTED'
    Complete = 'COMPLETE'
    Returned = 'RETURNED'
    PendingPrinting = 'PENDING_PRINTING'
    Void = 'VOID'
    StopPayment = 'STOP_PAYMENT'


class TransferRejectReason(Enum):
    Compliance = 'COMPLIANCE'
    MarginCalls = 'MARGIN_CALLS'
    MissingPaperwork = 'MISSING_PAPERWORK'
    NeedsApproval = 'NEEDS_APPROVAL'
    Nsf = 'NSF'
    OutstandingAcat = 'OUTSTANDING_ACAT'
    PerBrokerRequest = 'PER_BROKER_REQUEST'
    PerCorrespondentRequest = 'PER_CORRESPONDENT_REQUEST'
    PrepayNotAuthorized = 'PREPAY_NOT_AUTHORIZED'
    RecentDepositHold = 'RECENT_DEPOSIT_HOLD'
    ReturnMail = 'RETURN_MAIL'
    ReferToMaker = 'REFER_TO_MAKER'
    UncollectedFunds = 'UNCOLLECTED_FUNDS'
    TokenNotRegisteredForThisAccount = 'TOKEN_NOT_REGISTERED_FOR_THIS_ACCOUNT'
    Other = 'OTHER'
    IncorrectDistributionType = 'INCORRECT_DISTRIBUTION_TYPE'
    TaxWithholdingMismatch = 'TAX_WITHHOLDING_MISMATCH'
    StaleTransfer = 'STALE_TRANSFER'
    Foreign3rdParty = 'FOREIGN_3RD_PARTY'
    ExceedsDailyDepositLimit = 'EXCEEDS_DAILY_DEPOSIT_LIMIT'


class TransferDisbursementType(Enum):
    PartialBalance = 'PARTIAL_BALANCE'
    FullBalance = 'FULL_BALANCE'


class IraContributorType(Enum):
    Regular = 'REGULAR'
    Employee = 'EMPLOYEE'
    Employer = 'EMPLOYER'
    Recharacterization = 'RECHARACTERIZATION'
    Rollover60Day = 'ROLLOVER_60_DAY'
    RolloverDirect = 'ROLLOVER_DIRECT'
    Transfer = 'TRANSFER'
    TrusteeFee = 'TRUSTEE_FEE'
    Conversion = 'CONVERSION'


class IraDistributionReason(Enum):
    Normal = 'NORMAL'
    Disability = 'DISABILITY'
    Sosepp = 'SOSEPP'
    Premature = 'PREMATURE'
    Death = 'DEATH'
    ExcessContributionRemovalBeforeTaxDeadline = 'EXCESS_CONTRIBUTION_REMOVAL_BEFORE_TAX_DEADLINE'
    ExcessContributionRemovalAfterTaxDeadline = 'EXCESS_CONTRIBUTION_REMOVAL_AFTER_TAX_DEADLINE'
    RolloverToQualifiedPlan = 'ROLLOVER_TO_QUALIFIED_PLAN'
    RolloverToIra = 'ROLLOVER_TO_IRA'
    Transfer = 'TRANSFER'
    RecharacterizationPriorYear = 'RECHARACTERIZATION_PRIOR_YEAR'
    RecharacterizationCurrentYear = 'RECHARACTERIZATION_CURRENT_YEAR'
    Conversion = 'CONVERSION'
    ManagementFee = 'MANAGEMENT_FEE'
    PrematureSimpleIraLessThan2Years = 'PREMATURE_SIMPLE_IRA_LESS_THAN_2_YEARS'
    NormalRothIraGreaterThan5Years = 'NORMAL_ROTH_IRA_GREATER_THAN_5_YEARS'


class IraTaxWithholdingType(Enum):
    Fixed = 'FIXED'
    Percentage = 'PERCENTAGE'
