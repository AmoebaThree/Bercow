if __name__ == '__main__':
    import os, redis

    print('ORDER')
    os.system("amixer set PCM unmute")
    os.system("amixer set PCM 100%")
    r = redis.Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT", "6379")), db=0)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe('bercow')
    print('ORDER')

    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        for message in p.listen():
            cmd = message["data"]
            filepath = dir_path + "/Audio/" + cmd + ".WAV"
            if os.path.isfile(filepath):
                os.system("aplay " + filepath + " &")
            
    except:
        p.close()
        print("ORDER")