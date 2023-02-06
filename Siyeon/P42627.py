import heapq


def findWaiting(jobs, time):
    waitJobs = []

    for job in jobs:
        arriveTime = job[0]
        workTime = job[1]

        if arriveTime <= time:
            heapq.heappush(waitJobs, [workTime, arriveTime])

    shortest = heapq.heappop(waitJobs)
    waitTime = (time + shortest[0]) - shortest[1]
    time += shortest[0]

    jobs.remove([shortest[1], shortest[0]])

    return [time, waitTime]


def solution(jobs):
    num = len(jobs)
    answer = 0
    time = 0
    heapq.heapify(jobs)

    job = heapq.heappop(jobs)
    answer = job[1]
    time = job[0] + job[1]

    while len(jobs) > 0:
        # 작업을 수행하고 있지 않은 경우
        if jobs[0][0] > time:
            time = jobs[0][0] + jobs[0][1]
            answer += jobs[0][1]
            heapq.heappop(jobs)
        # 작업 수행 중에 job이 들어온 경우
        else:
            arr = findWaiting(jobs, time)
            time = arr[0]
            answer += arr[1]

    print({"final": answer//num})
    return answer // num