a = int(input())

if a in range(1,5):
    print("few")
elif a in range(5,10):
    print("several")
elif a in range(10, 20):
    print("pack")
elif a in range(20, 50):
    print("lots")
elif a in range(50, 100):
    print("horde")
elif a in range(100, 250):
    print("throng")
elif a in range(250, 500):
    print("swarm")
elif a in range(500,1000):
    print("zounds")
elif a>=1000:
    print("legion")