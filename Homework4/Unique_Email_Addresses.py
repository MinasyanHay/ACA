def super_mail(mail):
    local_name , domain = mail.split("@")
    if "+" in local_name:
        local_name = local_name[:local_name.index("+")]
    if "." in local_name:
        local_name = "".join(local_name.split("."))
    return "".join([local_name,"@",domain])

def Unique_mail(emails):
    Unique = set()
    for mail in emails:
        Unique.add(super_mail(mail))
    return len(Unique)

#Emails = ["test.email+alex@leetcode.com" , "test.e.mail+bob.cathy@leetcode.com" , "testemail+david@lee.tcode.com"]
Emails = [ "a@leetcode.com" , "b@leetcode.com" , "c@leetcode.com" ]
print(Unique_mail(Emails))
