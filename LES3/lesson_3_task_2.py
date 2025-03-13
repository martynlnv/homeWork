from smartphone import Smartphone

Catalog = [
    Smartphone("< Samsung >", "< Galaxy >" , "<< +7(911)-212-21-12 >>"),
    Smartphone("< Xiaomi >",  "< Lite >",   "<< +7(921)-345-34-41 >>"),
    Smartphone("< iPhone >",  "< Pro Max >", " << +7(922)-991-54-11 >>"),
    Smartphone("< Infinix >", "< Note > ", "<< +7(981)-865-87-86 >>"),
    Smartphone("< Nokia >", "< Eseries >", "<< +7(812)-244-24-24 >>")
]

for smartphone in Catalog:
    print(f"{smartphone.stamp} - {smartphone.model}.  {smartphone.number}")