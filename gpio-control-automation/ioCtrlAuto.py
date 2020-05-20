# For Linux GPIO Control
# Automatically gives bash control statements until GPIO number is clear

for i in range(128):
    print("echo ", end='')
    print(i, end='')
    print(" > /sys/class/gpio/export")
    
    print("echo \"high\" > /sys/class/gpio/gpio", end='')
    print(i, end='')
    print("/direction")
    
    print("echo 1 > /sys/class/gpio/gpio", end='')
    print(i, end='')
    print("/value")
    
    while 1:
        key = input().strip()

        if key == 'q':
            break
        else:
            try:
                intKey = int(key)
                if 0 <= intKey < 128:
                    print("echo ", end='')
                    print(key, end='')
                    print(" > /sys/class/gpio/export")
                    
                    print("echo \"high\" > /sys/class/gpio/gpio", end='')
                    print(key, end='')
                    print("/direction")
                    
                    print("echo 1 > /sys/class/gpio/gpio", end='')
                    print(key, end='')
                    print("/value")
                else:
                    continue
            except:
                continue