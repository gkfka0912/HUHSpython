'''
1. https:// 제외
2. 첫번째 . 이후 제외
3. [0:3] + len + count + "!"
'''

domain=input()
site=(domain.replace("https://",""))
site=(site[:(site.find("."))])
pw=site[0:3]+str(len(site))+str(site.count("e"))+"!"
print(f"생성된 비밀번호 : {pw}")