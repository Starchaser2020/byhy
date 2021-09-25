with open('teacher.txt',mode='r',encoding='utf8') as f:
    f.readline()
    info = []
    teacherInfo = {}
    for line in f.readlines():
        if not line.strip():
            continue
        id = int(line.strip().split(';')[0])
        info = line.strip().split(';')[1:]
        teacherInfo[id] = info
    print(teacherInfo)
with open('course.txt',mode='r',encoding='utf8') as f:
    f.readline()
    info = []
    courseInfo = {}
    for line in f.readlines():
        if not line.strip():
            continue
        id = int(line.strip().split(';')[0])
        info = line.strip().split(';')[1:]
        courseInfo[id] = info
    print(courseInfo)

with open('teacher_course.txt',mode='r',encoding='utf8') as f:
    f.readline()
    for line in f.read().splitlines():
        if not line.strip():
            continue
        teacher_id = int(line.split(';')[0])
        course_id = int(line.split(';')[1])

        print(f"{teacherInfo[teacher_id][-1]:<8}:{courseInfo[course_id][0]}")



with open('teacher.txt',mode='r',encoding='utf8') as f:
    f.readline()
    info = []
    teacherInfo = {}
    for line in f.readlines():
        if not line.strip():
            continue
        id = int(line.strip().split(';')[0])
        info = line.strip().split(';')[1:]
        teacherInfo[id] = info
    print(teacherInfo)
