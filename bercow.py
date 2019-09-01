if __name__ == '__main__':
    import systemd.daemon, os, redis

    print('ORDER')
    os.system("amixer set PCM unmute")
    os.system("amixer set PCM 100%")
    r = redis.Redis(host='192.168.0.1', port=6379, db=0)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('bercow')
    print('ORDER')
    systemd.daemon.notify('READY=1')

    try:
        for message in p.listen():
            cmd = message["data"]
            filepath = "/home/pi/code/Bercow/Audio/" + cmd + ".WAV"
            if os.path.isfile(filepath):
                os.system("aplay " + filepath + " &")
            
    except:
        p.close()
        print("ORDER")