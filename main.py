from multiprocessing import Process
from rnn import rnn
from cnn import cnn

if __name__ == '__main__':
    models = [rnn, cnn]

    print('running models')
    processes = []
    for model in models:
        print('init process')
        process = Process(target=model)
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

