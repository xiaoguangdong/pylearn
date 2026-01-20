"""
    需求：有一个嵌套字典，存储了学生的课程成绩信息。 编写一个函数，
    计算每个学生的平均成绩，并返回一个新的字典，键为学生名字，值为平均成绩。
    {
        "Alice": {"Math": 85,"English": 90,"Science": 78},
        "Bob": {"Math": 92,"English": 88,"Science": 95},
        "Charlie": {"Math": 70,"English": 75,"Science": 80}
    }
"""
students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}
def cal_avg():
    res_dict = {}
    for name,course_scores in students.items():
        # print(name,course_scores)
        scores = sum(course_scores.values())
        avg_score = scores/len(course_scores)
        res_dict[name] = round(avg_score,2)
    return res_dict


print(cal_avg())
