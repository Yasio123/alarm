from machine import Pin
from utime import sleep

while True:
    # WYJSCIA
    l1 = Pin(15, Pin.OUT)  # LED-STATUS WYLACZONY
    l2 = Pin(14, Pin.OUT)  # LED-CZAS NA WYJSCIE
    l3 = Pin(13, Pin.OUT)  # LED-UZBROJENIE
    l4 = Pin(12, Pin.OUT)  # LED-ALARM
    s1 = Pin(20, Pin.OUT)  # SYGNALIZATOR/PRZEKAZNIK
    lon = Pin(25, Pin.OUT)
    # WEJSCIA
    p1 = Pin(5, Pin.IN, Pin.PULL_UP)  # PRZYCISK START
    c1 = Pin(17, Pin.IN, Pin.PULL_DOWN)  # CZUJKA RUCHU
    c1.value(0)
    # POKAZUJE STATUS CZUJKI NA L1
    l1.value(c1.value())

    lon.value(1)

    # FUNKCJA WYWOLANA CZUJKA
    # POKAZUJE STATUS CZUJKI NA L1

    def c1_change(p):
        l1.value(c1.value())


    # PRZERWANIE CZUJKI
    c1.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=c1_change)

    # LOGIKA ALARMU

    # CZEKAJ NA PRZYCISK
    while p1.value() == 1:
        pass

    l2.value(1)  # LED CZAS NA WYJSCIE
    sleep(20)  # ODCZEKAJ 10 SEKUND
    l2.value(0)

    # CZEKAJ NA ZADZIALANIE CZUJKI
    while c1.value() == 1:
        pass

    l3.value(1)  # ALARM UZBROJONY

    while c1.value() == 0:
        sleep(10)
        while c1.value() == 0:
            pass
    # ALARM!!
    sleep(5)
    l3.value(0)
    l4.value(1)
    s1.value(1)
    sleep(30)
    # ODCZEKAJ 30 SEKUND I WYLACZ
    l4.value(0)
    s1.value(0)
    sleep(10)
    l4.value(1)
    s1.value(1)
    sleep(30)
    l4.value(0)
    s1.value(0)
