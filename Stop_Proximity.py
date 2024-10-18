from controller import Robot

# Buat instance dari robot
robot = Robot()

# Atur timestep (interval waktu simulasi)
timestep = int(robot.getBasicTimeStep())

# Atur kecepatan motor
MAX_SPEED = 6.28  # Kecepatan maksimal motor e-puck

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set motor ke mode posisi tak terbatas agar terus bergerak
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Inisialisasi kecepatan awal
left_motor.setVelocity(MAX_SPEED)
right_motor.setVelocity(MAX_SPEED)

# Mengaktifkan sensor proximity pada e-puck
ps = []
for i in range(8):
    sensor = robot.getDevice('ps' + str(i))  # Dapatkan sensor proximity (ps0 hingga ps7)
    sensor.enable(timestep)  # Aktifkan sensor
    ps.append(sensor)

# Loop simulasi, robot akan bergerak maju sampai sensor proximity mendeteksi objek
while robot.step(timestep) != -1:
    # Membaca nilai sensor proximity
    ps_values = [sensor.getValue() for sensor in ps]
    
    # Jika ada sensor yang mendeteksi objek di depan, hentikan robot
    if ps_values[0] > 80.0 or ps_values[7] > 80.0:  # Sensor depan (ps0 dan ps7) mendeteksi objek
        left_motor.setVelocity(0)  # Hentikan roda kiri
        right_motor.setVelocity(0)  # Hentikan roda kanan
    else:
        # Robot akan bergerak maju jika tidak ada objek di depan
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)
