def titleize(string):
    title = string.split()
    ans = []
    for word in title:
        capitalized = word[0].upper() + word[1:]
        ans.append(capitalized)
    return " ".join(ans)

print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"