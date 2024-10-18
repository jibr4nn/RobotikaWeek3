from controller import Robot

# Buat instance dari robot
robot = Robot()

# Atur timestep (interval waktu simulasi)
timestep = int(robot.getBasicTimeStep())

# Atur kecepatan motor
MAX_SPEED = 6.28  # Maksimal kecepatan motor e-puck
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set motor ke mode posisi tak terbatas agar terus bergerak
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set kecepatan kedua motor agar robot bergerak maju
left_motor.setVelocity(MAX_SPEED)
right_motor.setVelocity(MAX_SPEED)

# Loop simulasi, berjalan terus selama simulasi aktif
while robot.step(timestep) != -1:
    # Robot akan terus bergerak maju
    pass
