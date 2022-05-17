from collections import Counter

phones = ['Iphone', 'Samsung', 'LG', 'Iphone', 'Iphone', 'LG']

count = Counter(phones)
print(count)
print(count['LG'])
print(count['Hello'])

text = 'Ехал Грека через реку, видит Грека в реке рак, сунул Грека в реку руку, рак за руку Грека цап'
text_count = Counter(text.lower().replace(' ', ''))
print(text_count)