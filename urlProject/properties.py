
# Base de la url
protocol = "https"
dominion = "www.banxico.org.mx"
path     = "cep-beta/go"
VpmKey   = "40113"
serialNo = "20210206"

UrlBasePath = protocol + "://"
UrlBasePath += dominion + "/"
UrlBasePath += path + "?"

parameter1 = VpmKey
parameter2 = serialNo

print(UrlBasePath)

mainSeparator = "|"
AESKey        = "1234567890abcdef"
