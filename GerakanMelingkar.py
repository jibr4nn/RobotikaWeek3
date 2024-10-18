from controller import Robot

# Buat instance dari robot
robot = Robot()

# Atur timestep (interval waktu simulasi)
timestep = int(robot.getBasicTimeStep())

# Atur kecepatan motor
MAX_SPEED = 6.28  # Kecepatan maksimal motor e-puck
SLOW_SPEED = MAX_SPEED * 0.5  # Kecepatan lebih lambat untuk roda kiri

# Mendapatkan motor kiri dan kanan
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set motor ke mode posisi tak terbatas agar terus bergerak
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set kecepatan roda kiri lebih lambat dari roda kanan untuk bergerak melingkar
left_motor.setVelocity(SLOW_SPEED)
right_motor.setVelocity(MAX_SPEED)

# Loop simulasi, robot akan terus bergerak melingkar selama simulasi berjalan
while robot.step(timestep) != -1:
    pass
