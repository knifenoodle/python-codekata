# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 송원우
# 작성일: 2026. 01. 21. 11:10:24

def solution(n, k):
    answer = n * 12000 + k * 2000 - (n//10 * 2000)
    return answer