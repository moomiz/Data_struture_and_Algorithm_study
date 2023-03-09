# 신고결과 받기 
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
K = 2
#중복 신고 제거
report = list(set(report))
# 신고한 id 저장 list
report_id = dict.fromkeys(id_list,set())
#신고된 id 저장 list
reported_id = {i:0 for i in id_list}

for i in report: 
    # 공백으로 분류 신고한사람 :A, 신고당한사람: B
    A,B = i.split()
    reported_id[B] += 1
    report_id[A].add(B)
print(reported_id)
print(report_id)

# 정지된 사람 구하기  
stop_list =set()
for j in reported_id.items():
    if j[1] >= K:
        stop_list.add(j[0])
print(stop_list)

# 신고 리포트 받을 사람 
