# Demo code for testing various conditions

num=23
print(num>10)

custtype="member"
amt=2550

if custtype=="member" and amt>2500:
    disc=float(amt)*10/100
else:
    disc=float(amt)*5/100

netbill=amt-disc
print("Discount is %.2f"%disc)
print("NetBill is %.2f"%netbill)

nm="soham"
if nm in ["amir","cruise"]:
    print("found in the movies team")
elif nm in ["griezmann","lewandowsky","soham"]:
    print("found in the sports team")
else:
    print("not in any team")


num1=[12,23,34]
num2=[45,56,67]
print(not num1==num2)


# content of sohamglobal.com