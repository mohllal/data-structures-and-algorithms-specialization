# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to simulate jobs parallel processing.

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

# O(n^2) time and O(n) space
def assign_jobs_naive(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

if __name__ == "__main__":
    n_workers, m_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == m_jobs

    assigned_jobs = assign_jobs_naive(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)
