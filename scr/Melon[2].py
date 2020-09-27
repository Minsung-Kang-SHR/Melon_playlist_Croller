###############################################################
# Melon 플레이리스트의 받아온 정보를 오래된 플레이리스트 순으로 정리한다.
# 역으로 정렬함으로서 작업순서를 반대로 설정하여준다. 

# 작성자 : 강민성
# 작성일 : 2020.09.14
# 최종 수정일 : 2020.09.19
###############################################################
#####################     Import     ##########################
import csv

#####################     Main     ##########################

f = open('..\csv\melon[1]_csv\melon_play_list.csv', 'r', encoding='utf8')     
fout = open('..\ws\workspace.csv', 'w', encoding='utf8')

rdr = csv.reader(f)

for line in reversed(list(rdr)):
    table = str.maketrans('\/:*?"<>|', '---------')
    fout.write(line[0])
    fout.write(",")
    fout.write(line[1].translate(table))
    fout.write("\n")
    
f.close()
fout.close()
