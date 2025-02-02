
from properties import *
from functions import *
from data import *

CEPString = serialNo + mainSeparator.join([processDate,queryCriteria,queryValue,pmtIssuerKey,pmtRecipientKey,benefAccount,pmtAmount])

CEPCipherString    = AESCipher128Cbc(CEPString,AESKey)
CEPSanitizedString = stringSanitizer(CEPCipherString)

CEPurl = UrlBasePath + "i="
CEPurl += parameter1 + "&s="
CEPurl += parameter2 + "&d="
CEPurl += CEPSanitizedString

print(CEPurl)
