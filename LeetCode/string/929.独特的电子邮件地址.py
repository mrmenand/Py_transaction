#929 独特的电子邮件
class Solution:
    def numUniqueEmails(self,emails):
            # emails: List[str]) -> int:
            email_set = set()
            for email in emails:
                name,domain = email.split("@")
                # name = name[:name.find("+")].replace(".","")
                name = name.split("+")[0].replace(".","")
                email_set.add(name + "@" + domain)

            return len(email_set)


