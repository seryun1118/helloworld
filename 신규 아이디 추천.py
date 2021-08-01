answer = ''
new_id = "...!@BaT#*..y.abcdefghijklm"
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
new_id = new_id.lower()
print("1단계 : " + new_id)


# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
for x in new_id:
    if( (x.isalpha() == False) and (x.isdigit() == False) and (x != '-') and (x != '_') and (x != '.')):
        new_id = new_id.replace(x,'')
print("2단계 : " + new_id)

# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
flag = False
temp = list(new_id)
new_id = ''
for x in range(len(temp)):
    if(temp[x] == '.'):
        if(flag == False):
            new_id = new_id + temp[x]
            flag = True
    else:
        new_id = new_id + temp[x]
        flag = False
print("3단계 : " + new_id)

# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
if(len(new_id)>0):
    if(new_id[0] == '.'):
        new_id = new_id[1:]
    elif(new_id[-1] == '.'):
        new_id = new_id[:-1]
print("4단계 : " + new_id)

# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
if(new_id == ""):
    new_id = 'a'
print("5단계 : " + new_id)

# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
if(len(new_id)>=16):
    new_id = new_id[0:15]
while(new_id[-1] == '.'): # 맨끝의 마침표가 2개 이상일수있음
    new_id = new_id[:len(new_id) - 1]
print("6단계 : " + new_id)

# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
if(len(new_id)<=2):
    add = new_id[len(new_id)-1]
    while(len(new_id)<3):
       new_id = new_id + add
print("7단계 : " + new_id)
