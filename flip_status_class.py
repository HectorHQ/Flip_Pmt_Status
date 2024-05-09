from email import header
import requests
import pandas as pd


def connect_website(bearer_token):
    headers = {
        "authority": "api.getnabis.com",
        "accept": "*/*",
        "accept-language": "es-ES,es;q=0.9", #"en-GB,en-US;q=0.9,en;q=0.8"
        "authorization": bearer_token,
        # Already added when you pass json=
        # 'content-type': 'application/json',
        "origin": "https://app.getnabis.com",
        "referer": "https://app.getnabis.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
    }
    return headers



def all_admin_orders_accounting_page(headers,order_number):
    json_data = {
        "operationName": "AllAdminOrdersAccountingPage",
        "variables": {
            "pageInfo": {
                "numItemsPerPage": 25,
                "orderBy": [
                    {
                        "attribute": "date",
                        "order": "DESC",
                    },
                    {
                        "attribute": "createdAt",
                        "order": "DESC",
                    },
                ],
                "page": 1,
            },
            "search": order_number,
            "status": [
                "DELIVERED",
                "DELIVERED_WITH_EDITS",
                "DELAYED",
                "REJECTED",
                "ATTEMPTED",
            ],
        },
        "query": "query AllAdminOrdersAccountingPage($organizationId: ID, $search: String, $status: [OrderStatusEnum], $paymentStatus: [OrderPaymentStatusEnum], $disputeStatus: [OrderDisputeStatus!], $start: DateTime, $end: DateTime, $paymentProcessedAtStart: DateTime, $paymentProcessedAtEnd: DateTime, $paymentSentAtStart: DateTime, $paymentSentAtEnd: DateTime, $paidAtStart: DateTime, $paidAtEnd: DateTime, $irn: String, $orderFees: [String], $pageInfo: PageInfoInput, $collectionStatus: [BrandFeesCollectionCollectionStatusEnum]) {\n  viewer {\n    allAdminAccountingOrders(organizationId: $organizationId, search: $search, status: $status, irn: $irn, paymentStatus: $paymentStatus, disputeStatus: $disputeStatus, start: $start, end: $end, paymentProcessedAtStart: $paymentProcessedAtStart, paymentProcessedAtEnd: $paymentProcessedAtEnd, paymentSentAtStart: $paymentSentAtStart, paymentSentAtEnd: $paymentSentAtEnd, paidAtStart: $paidAtStart, paidAtEnd: $paidAtEnd, orderFees: $orderFees, pageInfo: $pageInfo, collectionStatus: $collectionStatus) {\n      results {\n        id\n        adminNotes\n        action\n        accountingNotes\n        ACHAmountCollectedRetailer\n        ACHAmountPaidBrand\n        internalNotes\n        createdAt\n        creditMemo\n        date\n        daysTillPaymentDue\n        distroFees\n        dueToBrand\n        discount\n        surcharge\n        edited\n        exciseTax\n        exciseTaxCollected\n        extraFees\n        gmv\n        gmvCollected\n        wholesaleGmv\n        priceDifference\n        irn\n        manifestGDriveFileId\n        apSummaryGDriveFileId\n        apSummaryS3FileLink\n        invoicesS3FileLink\n        packingListS3FileLink\n        mustPayPreviousBalance\n        nabisDiscount\n        name\n        notes\n        number\n        isSampleDemo\n        parentOrder {\n          id\n          totalGMV\n          shouldRemoveMinFee\n          __typename\n        }\n        paymentStatus\n        paymentTermsRequestStatus\n        hasSingleQBInvoice\n        hasMultiQBInvoices\n        hasMultiAQBInvoice\n        hasMultiBQBInvoice\n        hasMultiCQBInvoice\n        hasMultiC1QBInvoice\n        hasMultiC2QBInvoice\n        isAfterQuickbooksDeploy\n        lastPaymentTermOrderChange {\n          submitter {\n            id\n            firstName\n            lastName\n            isAdmin\n            __typename\n          }\n          id\n          description\n          createdAt\n          __typename\n        }\n        orderFees {\n          ...feeOrderFragment\n          __typename\n        }\n        pricingFee\n        pricingPercentage\n        basePricing {\n          pricingFee\n          pricingPercentage\n          __typename\n        }\n        status\n        creator {\n          id\n          email\n          firstName\n          lastName\n          __typename\n        }\n        licensedLocation {\n          ...licensedLocationFragment\n          __typename\n        }\n        organization {\n          id\n          doingBusinessAs\n          alias\n          name\n          owner {\n            id\n            email\n            firstName\n            lastName\n            __typename\n          }\n          __typename\n        }\n        site {\n          id\n          name\n          address1\n          address2\n          city\n          state\n          zip\n          pocName\n          pocPhoneNumber\n          pocEmail\n          licensedLocationId\n          licensedLocation {\n            id\n            __typename\n          }\n          __typename\n        }\n        paidAt\n        paymentMethod\n        remittedAt\n        factorStatus\n        calculateMoneyValues {\n          subtotal\n          orderDiscount\n          lineItemDiscounts\n          totalExciseTax\n          totalBalance\n          discountedSubtotal\n          taxRate\n          netOffTotal\n          __typename\n        }\n        nabisManifestNotes\n        referrer\n        orderFiles {\n          ...orderFileFragment\n          __typename\n        }\n        writeOffReasons\n        paymentSentAt\n        processingAt\n        ...lastAccountingOrderIssues\n        brandFeesCollection {\n          ...BrandFeesCollectionFragment\n          user {\n            id\n            firstName\n            lastName\n            email\n            __typename\n          }\n          __typename\n        }\n        willAutoRegenerateInvoices\n        __typename\n      }\n      pageInfo {\n        page\n        numItemsPerPage\n        orderBy {\n          attribute\n          order\n          __typename\n        }\n        totalNumItems\n        totalNumPages\n        __typename\n      }\n      nextOrders {\n        number\n        date\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment feeOrderFragment on OrderFee {\n  id\n  feeId\n  feeName\n  feePrice\n  feeNotes\n  createdBy {\n    firstName\n    lastName\n    email\n    __typename\n  }\n  fee {\n    ...feeFragment\n    __typename\n  }\n  __typename\n}\n\nfragment feeFragment on Fee {\n  id\n  basePrice\n  description\n  name\n  feeType\n  groupTag\n  startDate\n  endDate\n  isArchived\n  __typename\n}\n\nfragment licensedLocationFragment on LicensedLocation {\n  id\n  name\n  address1\n  address2\n  city\n  state\n  zip\n  siteCategory\n  lat\n  lng\n  billingAddress1\n  billingAddress2\n  billingAddressCity\n  billingAddressState\n  billingAddressZip\n  warehouseId\n  isArchived\n  doingBusinessAs\n  noExciseTax\n  phoneNumber\n  printCoas\n  hoursBusiness\n  hoursDelivery\n  deliveryByApptOnly\n  specialProtocol\n  schedulingSoftwareRequired\n  schedulingSoftwareLink\n  centralizedPurchasingNotes\n  payByCheck\n  collectionNotes\n  deliveryNotes\n  collect1PocFirstName\n  collect1PocLastName\n  collect1PocTitle\n  collect1PocNumber\n  collect1PocEmail\n  collect1PocAllowsText\n  collect1PreferredContactMethod\n  collect2PocFirstName\n  collect2PocLastName\n  collect2PocTitle\n  collect2PocNumber\n  collect2PocEmail\n  collect2PocAllowsText\n  collect2PreferredContactMethod\n  delivery1PocFirstName\n  delivery1PocLastName\n  delivery1PocTitle\n  delivery1PocNumber\n  delivery1PocEmail\n  delivery1PocAllowsText\n  delivery1PreferredContactMethod\n  delivery2PocFirstName\n  delivery2PocLastName\n  delivery2PocTitle\n  delivery2PocNumber\n  delivery2PocEmail\n  delivery2PocAllowsText\n  delivery2PreferredContactMethod\n  unmaskedId\n  qualitativeRating\n  creditRating\n  trustLevelNabis\n  trustLevelInEffect\n  isOnNabisTracker\n  locationNotes\n  infoplus\n  w9Link\n  taxIdentificationNumber\n  sellerPermitLink\n  nabisMaxTerms\n  __typename\n}\n\nfragment orderFileFragment on OrderFile {\n  id\n  type\n  s3Link\n  mimeType\n  notes\n  createdAt\n  updatedAt\n  orderId\n  __typename\n}\n\nfragment lastAccountingOrderIssues on AccountingOrder {\n  lastDispute {\n    id\n    reason\n    initiatedNotes\n    initiatedAt\n    issueType\n    resolvedAt\n    __typename\n  }\n  lastNonpayment {\n    id\n    reason\n    initiatedNotes\n    initiatedAt\n    issueType\n    __typename\n  }\n  __typename\n}\n\nfragment BrandFeesCollectionFragment on BrandFeesCollection {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  submitterId\n  collectionStatus\n  collectionStatusUpdatedAt\n  notes\n  __typename\n}\n",
    }

    response = requests.post(
        "https://api.getnabis.com/graphql/admin", headers=headers, json=json_data
    )
    status = response.status_code
    text_response = response.text
    return response,status,text_response



def UpdateOrder_NET_TERMS_PAID(headers,qb_invoice_data):
        
    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'NET_TERMS_PAID',
                'writeOffReasons': [],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)

    status = response.status_code
    text_response = response.text
    return status,text_response



def UpdateOrder_COD_PAID(headers,qb_invoice_data):
    
    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'COD_PAID',
                'writeOffReasons': [],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response

def payment_method(headers,qb_invoice_data,pmt_method):
    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentMethod': pmt_method,
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response


def UpdateOrder_REMITTED(headers,qb_invoice_data):

    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'REMITTED',
                'writeOffReasons': [],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response


def UpdateOrder_PARTIAL_PAID(headers,qb_invoice_data):

    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'PARTIAL_PAID',
                'writeOffReasons': [],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response


def amount_collected(headers,qb_invoice_data,gmv_collected,tax_collected):
    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'gmvCollected': gmv_collected,
                'exciseTaxCollected': tax_collected,
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response


def UpdateOrder_SELF_COLLECTED(headers,qb_invoice_data):

    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'SELF_COLLECTED',
                'writeOffReasons': [],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response


def UpdateOrder_PROCESSING(headers,qb_invoice_data):

    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'PROCESSING',
                'writeOffReasons': [],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response


def update_Brand_fee_90_days(headers,invoice_data):
    json_data = {
        'operationName': 'UpdateBrandFeesCollection',
        'variables': {
            'id': invoice_data['id'],
            'collectionStatus': 'COLLECTED',
            'notes': '',
        },
        'query': 'mutation UpdateBrandFeesCollection($id: ID!, $collectionStatus: BrandFeesCollectionCollectionStatusEnum, $notes: String!) {\n  updateBrandFeesCollection(id: $id, collectionStatus: $collectionStatus, notes: $notes)\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response


def update_write_off(headers,qb_invoice_data,defunct):
    
    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'WRITE_OFF',
                'writeOffReasons': [
                    defunct,
                ],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHACRetailerUnconfirmed\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  mustPayExternalBalance\n  externalPaymentMin\n  externalPaymentDesired\n  externalPaymentNotes\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  isCreditMemoLocked\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }
    
    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    status = response.status_code
    text_response = response.text
    return status,text_response


def UpdateOrder_THIRD_PARTY_COLLECTIONS(headers,qb_invoice_data):

    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'THIRD_PARTY_COLLECTIONS',
                'writeOffReasons': [],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    
    status = response.status_code
    text_response = response.text
    return status,text_response


def UpdateOrder_UNPAID(headers,qb_invoice_data):

    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data['id'],
                'paymentStatus': 'UNPAID',
                'writeOffReasons': [],
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    
    status = response.status_code
    text_response = response.text
    return status,text_response


if __name__ == '__main__':
    headers = connect_website()
    all_admin_orders_accounting_page()
    UpdateOrder_COD_PAID()
    UpdateOrder_NET_TERMS_PAID()
    payment_method()
    UpdateOrder_REMITTED()
    UpdateOrder_PARTIAL_PAID()
    amount_collected()
    UpdateOrder_SELF_COLLECTED()
    update_Brand_fee_90_days()
    UpdateOrder_PROCESSING()
    update_write_off()
    UpdateOrder_THIRD_PARTY_COLLECTIONS()
    UpdateOrder_UNPAID()
    
