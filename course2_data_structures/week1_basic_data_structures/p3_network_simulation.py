# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to simulate network packet processing.
# Packets arrive in some order. For each packet number 𝑖, you know the time when it arrived 𝐴𝑖 and the time it takes the processor to process it 𝑃𝑖 (both in milliseconds). 
# There is only one processor, and it processes the incoming packets in the order of their arrival. 
# If the processor started to process some packet, it doesn’t interrupt or stop until it finishes the processing of this packet, and the processing of packet 𝑖 takes exactly 𝑃𝑖 milliseconds.

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    # O(n)
    def process(self, request):
        already_processed = self.finish_time[0] if len(self.finish_time) > 0 else None
        
        while already_processed and already_processed <= request.arrived_at:
            self.finish_time.pop(0)
            if len(self.finish_time) == 0:
                break
            already_processed = self.finish_time[0]
        
        packets_in_buffer = len(self.finish_time)
        if packets_in_buffer == self.size:
            return Response(True, -1)
        elif packets_in_buffer == 0:
            started_at = request.arrived_at
        else:
            started_at = self.finish_time[-1]
        
        finished_at = started_at + request.time_to_process
        self.finish_time.append(finished_at)
        return Response(False, started_at)

# O(n)
def process_requests(requests, buffer):
    responses = []
    for request in requests:
        response = buffer.process(request)
        responses.append(response)
    return responses

if __name__ == "__main__":
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        request = Request(arrived_at, time_to_process)
        requests.append(request)

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)