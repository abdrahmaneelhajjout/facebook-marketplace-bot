# -*- coding: utf-8 -*-

##############################
#                            #
#        MarketBot v0.1      #
#          By ModzDev_       #
#                            #
##############################

# Enter your email Facebook account
email = "email.test@exemple.com"
# Enter your password Facebook account
password = "AwesomePass"
# Enter your phone number
phone_number = "01 02 03 04 05"

message_mappings = {
    "Cet article est-il toujours disponible ?": """
    🇫🇷 نعم، هذا المنتج متاح دائمًا.
    لدينا أيضًا منتجات أخرى في المخزون.
    تفضل بزيارتنا!
    """,

    "Cet article m’intéresse.": """
    📢 رائع، سنسعد بمساعدتك!
    أي منتج يثير اهتمامك؟
    """,

    "Cet article est-il disponible ?": "Your response here...",
    "Is this still available?": "Your response here...",
    "Est-ce toujours disponible ?": "Your response here...",
    "Isto está disponível?": "Your response here...",
    "Hola, ¿sigue disponible?": "Your response here...",
    "È ancora disponibile?": "Your response here...",
    "Bu ürün hâlâ satılık mı?": "Your response here...",
    "¿Sigue disponible?": "Your response here...",
}


deliver_message = """
LE MAGASIN LIVRE UNIQUEMENT DES TELEPHONES NEUFS !
Les prix des téléphones seront légèrement plus chèrs car ils sont comme neuf. Le paiement se fera en espèce ou CB uniquement.

Pour prévoir une livraison, veuillez me contacter par SMS au {PHONE_NUMBER} et préciser votre numéro de téléphone valide, adresse complète et une carte d'identité.
""".format(PHONE_NUMBER=phone_number)

status_phone_message = """
Tous nos téléphones sont commes neufs. Les prix affichés sont ceux des téléphones les plus abîmés. En revanche, nous avons des téléphone d'occasions, comme neufs, sans traces d'usures. Les prix pour ces derniers sont bien entendu plus élevé.
"""

shop_adress_message = """
Le magasin se situe au 154 boulevard Berthier 75017, Métro 3: Porte de Champerret, RER C Pereire
"""
