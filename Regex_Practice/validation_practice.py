import re


def extractPhoneNumbers(given):
    phoneRegex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phoneRegex.findall(given)


def isPhoneNumber(given):
    phoneRegex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phoneRegex.search(given)
    if match:
        return True
    return False


print(extractPhoneNumbers("Call me at 469 522-6940 or 435 596-5069"))
print(isPhoneNumber("435 549 5435"))
print(isPhoneNumber("534 456-5043"))


def isValidTime(string):
    timeRegex = re.compile(r'^\d{1,2}:\d{2}$')
    match = timeRegex.search(string)
    if match:
        return True
    return False


print(isValidTime("10:45"))
print(isValidTime("100:45"))
print(isValidTime("2:45"))


def parseBytes(string):
    bytesRegex = re.compile(r'\b[01]{8}\b')
    return bytesRegex.findall(string)


print(parseBytes("my data is:01011101 323 0101 01010010"))


def parseDate(string):
    dateRegex = re.compile(r'\b(\d{2})[/,.](\d{2})[/,.](\d{4})\b')
    match = dateRegex.search(string)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3)}


print(parseDate("12/04/2004"))

def censor(given):
    censorRegex = re.compile(r"""frack([a-z]+)?""", re.I)
    result = censorRegex.sub("CENSORED",given)
    return result

print(censor("frack no"))