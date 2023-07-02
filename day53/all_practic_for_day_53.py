import re
# Практика регулярных выражений

s = "напишите ваш мейл home.work@gmail.com"

res = r"(([a-z0-9._-]+)@([a-z0-9._-]+\.[a-z]{2}))"
resss = re.findall(res, s)
print(resss)

g = "Кусочек строки, я пишу на питоне. В 1941 году маршал Василий прорвал оборону фашистов, убив 5000 врагов, проехав 200 км    "
res = r"^Кусочек"
resss = re.findall(res, g)
print(resss)