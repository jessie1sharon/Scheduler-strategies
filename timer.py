# jessica Llanos
import sys
import Queue as queue


class Process:

    def __init__(self, arrivetime, arrivetime1, runtime, runtime1, runtime2):
        self.arrive = int(arrivetime)
        self.arrive1 = int(arrivetime1)
        self.runTime = int(runtime)
        self.runTime1 = int(runtime1)
        self.runTime2 = int(runtime2)
        self.done = 0


def FCFS(arrivel):
    mean = 0                          # mean turnaround
    p = 0                             # location in the array
    y = 0                             # which iteration is it
    waiting = 0
    while p < len(arrivel):
        if arrivel[p].runTime == 0:   # if the process doesnt need time
            p += 1
            continue
        if y == 0:                    # if its the first iteration with rum time
            mean += arrivel[p].runTime
            summ = mean + arrivel[p].arrive
            waiting = summ
            p += 1
            y += 1
        else:
            if arrivel[p].arrive > waiting:      # if the next process arrives after the last process finished
                y -= 1
            else:
                waiting += arrivel[p].runTime         # the waiting time
                summ = waiting - arrivel[p].arrive
                mean += summ                           # the mean turnaround
                p += 1
    mean = float(mean)
    mean = mean/len(arrivel)
    print("FCFS: mean turnaround = {}".format(mean))   # printing the mean


def LCFS_NP(arrivel1):
    mean = 0                                # mean turnaround
    p = 0                                   # location in the array
    y = 0                                   # which iteration is it
    t = 0
    waiting = 0
    w = 0                                   # w = 0 then enter , w = 1 then we are done
    while p < len(arrivel1) and w == 0:
        if arrivel1[p].runTime == 0:        # if the process doesnt need time
            p += 1
            continue
        if y == 0:                          # if its the first iteration with rum time
            mean += arrivel1[p].runTime
            summ = mean + arrivel1[p].arrive
            waiting = summ
            p += 1
            y += 1
        else:
            if arrivel1[p].arrive > waiting:            # if the next process arrives after the last process finished
                y -= 1
            else:
                t += 1
                p += 1
                if p == len(arrivel1):                  # because of the 0 run time process
                    p -= 1
                    t -= 1
                if p == len(arrivel1)-1:
                    while t >= 0:
                        waiting += arrivel1[p].runTime                # the waiting time
                        summ = waiting - arrivel1[p].arrive
                        mean += summ                                  # the mean turnaround
                        p -= 1
                        t -= 1
                    w = 1                                             # we are done
                    continue

    mean = float(mean)
    mean = mean / len(arrivel1)
    print("LCFS(NP): mean turnaround = {}".format(mean))  # printing the mean


def LCFS_P(arrivel2):
    mean = 0                               # mean turnaround
    p = 0                                  # location in the array
    y = 0                                  # which iteration is it
    t = 0
    current_time = 0
    w = 0                                  # w = 0 then enter , w = 1 then we are done
    q1 = queue.LifoQueue()
    while p < len(arrivel2) and w == 0:
        if arrivel2[p].runTime == 0 and y == 0:       # if the process doesnt need time
            p += 1
            continue
        if p != len(arrivel2)-1:
            if arrivel2[p].arrive+arrivel2[p].runTime < arrivel2[p+1].arrive:
                mean += arrivel2[p].runTime
                y = 1
                p += 1
            if y == 0:                         # if its the first iteration with rum time
                current_time = arrivel2[p].arrive      # the current time were at is the arrivel time of the first process
                if current_time == arrivel2[p+1].arrive:       # if two or more processes entered the same time
                    q1.put(arrivel2[p])                        # putting the process in lifo queue
                    p += 1
                    continue
                if current_time+1 == arrivel2[p+1].arrive:       # if the next process starts one second after
                    current_time += 1
                    arrivel2[p].runTime -= 1                    # the current process did 1 sec
                    q1.put(arrivel2[p])                         # putting the process in lifo queue
                    p += 1
                    continue
                if current_time+2 == arrivel2[p+1].arrive:       # if the next process starts two second after
                    current_time += 2
                    arrivel2[p].runTime -= 2                    # the current process did 2 sec
                    q1.put(arrivel2[p])                         # putting the process in lifo queue
                    if arrivel2[p].runTime == 0:
                        item = q1.get()
                        t += 2
                    p += 1
                    continue
                if current_time+3 == arrivel2[p+1].arrive:       # if the next process starts two second after
                    current_time += 3
                    arrivel2[p].runTime -= 3                    # the current process did 2 sec
                    q1.put(arrivel2[p])                         # putting the process in lifo queue
                    p += 1
                    continue
        if p == len(arrivel2)-1:                       # if were in the end of the array
            mean += arrivel2[p].runTime
            current_time += mean
            p -= 1
            y = 1
            if q1.empty():
                w = 1
                continue
        else:
            if arrivel2[p].runTime == 0:
                p -= 1
                continue
            item = q1.get()
            current_time += item.runTime
            waiting = current_time - item.arrive
            mean += waiting
            if q1.empty():
                w = 1
                continue
            p -= 1
    mean += t
    mean = float(mean)
    mean = mean / len(arrivel2)
    print("LCFS(P): mean turnaround = {}".format(mean))  # printing the mean


def RR(arrivel3):
    mean = 0              # mean turnaround
    p = 0                 # location in the array
    y = 0                 # which iteration is it
    t = 0                 # to see if we need to start the next process in a long time
    w = 0                 # if we are done
    s = 0                 # if we started already
    waiting = 0           # to check if all process are done
    current_time = 0
    while p < len(arrivel3) and w == 0:

        if y == 0:       # if the process doesnt need time
            if arrivel3[p].runTime1 == 0:
                arrivel3[p].arrive = 0
                p += 1
                continue
        if p != len(arrivel3)-1 and s == 0:
            if t == 0 and arrivel3[p].arrive + arrivel3[p].runTime1 < arrivel3[p + 1].arrive:       # if a long time past
                mean += arrivel3[p].runTime1
                arrivel3[p].runTime1 -= arrivel3[p].runTime1
                t = 1
                p += 1
            if y == 0:
                current_time = arrivel3[p].arrive       # in the first iteration current time is the sec the first process arrives
                s = 1
                y = 1
        if arrivel3[p].runTime1 == 1:                   # if we have just a sec left
            arrivel3[p].runTime1 -= 1
            current_time += 1                           # will move to the next process & add its turnaround
            mean += current_time - arrivel3[p].arrive
            arrivel3[p].arrive = 0
            p += 1
            continue
        if t == 0:
            if arrivel3[p].arrive != 0:                 # if thw process didnt finish yet
                current_time += 2                       # time quantum
                arrivel3[p].runTime1 -= 2
                if arrivel3[p].runTime1 == 0 and y == 1:        # if the process finished
                    mean += current_time - arrivel3[p].arrive
                    arrivel3[p].arrive = 0
            else:
                if p != len(arrivel3)-1:                 # if we at a done process - move on
                    p += 1
                    continue

        if p == len(arrivel3) - 1:                  # if were in the end of the array
            for r in arrivel3:
                waiting += r.runTime1
            if waiting == 0:                        # if all the tun time left is 0 then we are done
                w = 1
                continue
            if waiting == arrivel3[p].runTime1:     # if just the last process is left
                if waiting > 2:
                    mean += arrivel3[p].runTime1
                    w = 1
            waiting = 0
            p -= (len(arrivel3)-1)                  # start over
            continue
        if current_time > arrivel3[p+1].arrive:     # move to the next process
            p += 1

    mean = float(mean)
    mean = mean / len(arrivel3)
    print("RR: mean turnaround = {}".format(mean))  # printing the mean


def SJF(arrivel4):
    p = 0                                   # the location on the array
    y = 0                                   # what iteration are we
    mean = 0
    start_time = []
    exit_time = []
    s_time = arrivel4[0].arrive1
    sequence_of_process = []
    for j in range(len(arrivel4)):          # giving all the process a number of process
        arrivel4[j].arrive = j
    while 1:
        if arrivel4[p].runTime2 == 0 and y == 0:  # if the process doesnt need time
            s_time = arrivel4[p+1].arrive1
            arrivel4[p].done = 1
            p += 1
            continue
        ready_queue = []
        normal_queue = []
        temp = []
        for i in range(len(arrivel4)):
            if arrivel4[i].arrive1 <= s_time and arrivel4[i].done == 0:          # moving all processes to a corresponding queue
                temp.extend([arrivel4[i].arrive1, arrivel4[i].runTime2, arrivel4[i].arrive])
                ready_queue.append(temp)                       # if the process is ready
                temp = []
            elif arrivel4[i].done == 0:
                temp.extend([arrivel4[i].arrive1, arrivel4[i].runTime2, arrivel4[i].arrive])
                normal_queue.append(temp)                      # if the process hasnt began yet
                temp = []
        if len(ready_queue) == 0 and len(normal_queue) == 0:                     # if both queue are empty then we are done
            break
        if len(ready_queue) != 0:
            y = 1
            ready_queue.sort(key=lambda x: x[1])                       # Sort processes according to run Time
            start_time.append(s_time)
            s_time = s_time + 1                                        # 1 second past
            e_time = s_time                                            # the current time
            exit_time.append(e_time)
            sequence_of_process.append(ready_queue[0][2])
            for k in range(len(arrivel4)):
                if arrivel4[k].arrive == ready_queue[0][2]:            # finding the process that run right now
                    break
            arrivel4[k].runTime2 -= 1                                  # 1 sec past so the process run 1 sec more
            if arrivel4[k].runTime2 == 0:              # If run time of a process is 0, it means the process is completed
                arrivel4[k].done = 1                   # set the done flag
                exit_time.append(e_time)
                mean += e_time - arrivel4[k].arrive1                   # updating the mean
        if len(ready_queue) == 0:                           # if the ready queue is empty
            if s_time < normal_queue[0][0]:                 # if the next process comes after the last one finished
                s_time = normal_queue[0][0]                 # then move to the next process
            start_time.append(s_time)
            s_time = s_time + 1                             # 1 sec past
            e_time = s_time
            sequence_of_process.append(normal_queue[0][2])
            for k in range(len(arrivel4)):
                if arrivel4[k].arrive == normal_queue[0][2]:           # checking what process is running
                    break
            arrivel4[k].runTime2 -= 1                        # updating the run time of the process running that a sec past
            if arrivel4[k].runTime2 == 0 and y == 1:         # If run time of a process is 0, it means the process is completed
                arrivel4[k].done = 1
                exit_time.append(e_time)
                mean += e_time - arrivel4[k].arrive1      # updating the mean

    mean = float(mean)
    mean = mean / len(arrivel4)
    print("SJF: mean turnaround = {}".format(mean))  # printing the mean


def arrive_time(elem):
    return elem.arrive


if __name__ == "__main__":
    if len(sys.argv) != 2:                                # if the num of argv is wrong
        print("wrong number of arguments , try again")
        quit()
    argv = []
    for i, arg in enumerate(sys.argv):
        argv.append(arg)                                  # saving the name of the input file
    f = open(argv[1], "r")
    numOfProcess = f.readline()                           # saving the num of processes
    numOfProcess = int(numOfProcess)
    process = []
    j = 0
    while j < numOfProcess:                               # spliting the process arrivel time and run time
        line = f.readline()
        arrive, runnig = line.split(',')
        process.append(Process(arrive, arrive, runnig, runnig, runnig))        # coping the data to an array so I can use & modify
        j += 1
    f.close()
    process = sorted(process, key=arrive_time)            # sorting the processes by the arrivel time

    FCFS(process)
    LCFS_NP(process)
    LCFS_P(process)
    RR(process)
    SJF(process)
