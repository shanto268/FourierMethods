'''
considering all amplitude be 1
message signal(m)=Am*sin(2*π*fm*t)
carrier signal(c)=Ac*sin(2*π*fc*t)
modulated signal(y)=Ac*sin(2*π*fc*t + mi*sin(2*π*fm*t))
modulateion index(fi)= ffdev / ff
'''
fm = float(input('Message Frequency='))  #1
fc = float(input('Carrier Frequency='))  #25
mi = float(input('Modulation Index='))  #10
t = np.arange(0, 1, 0.001)

m = np.sin(2 * np.pi * fm * t)  #modulation wave

plt.plot(t, m)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Message Signal', fontsize=15)
plt.grid(True)
plt.savefig("message.png")
plt.show()

c = np.sin(2 * np.pi * fc * t)
#carrier wave

plt.plot(t, c)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Carrier Signal', fontsize=15)
plt.grid(True)
plt.savefig("carrier.png")
plt.show()

y = np.sin(
    2 * np.pi * fc * t +
    (mi * np.sin(2 * np.pi * fm * t)))  #Frequency changing w.r.t Message

plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('FM Signal', fontsize=15)
plt.grid(True)
plt.savefig("fm.png")
plt.show()
'''
user inputs--------
Message Frequency=1
Carrier Frequency=25
Modulation Index=10
'''
