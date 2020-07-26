import systemd.daemon
import os
import redis


def execute():
    print('ORDER')

    os.system('amixer set PCM unmute')
    os.system('amixer set PCM 100%')

    r = redis.Redis(host='192.168.0.1', port=6379,
                    db=0, decode_responses=True)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('bercow')

    r.publish('services', 'bercow.on')
    systemd.daemon.notify('READY=1')
    print('ORDER')

    try:
        for message in p.listen():
            cmd = message['data']
            filepath = '/home/pi/zoidberg-deploy/bercow/Audio/' + cmd + '.WAV'
            if os.path.isfile(filepath):
                r.publish('bercow.playing', cmd)
                os.system('aplay ' + filepath + ' &')

    except:
        p.close()
        r.publish('services', 'bercow.off')
        print('ORDER')


if __name__ == '__main__':
    execute()
