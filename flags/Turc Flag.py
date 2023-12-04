from PIL import Image, ImageDraw

# Dimensions du drapeau
width = 1200
height = 800


star_points = [
    (star_x, star_y - star_radius),
    (star_x + 0.5878 * star_radius, star_y + 0.809 * star_radius),
    (star_x - 0.9511 * star_radius, star_y + 0.309 * star_radius),
    (star_x + 0.9511 * star_radius, star_y + 0.309 * star_radius),
    (star_x - 0.5878 * star_radius, star_y + 0.809 * star_radius)
]
draw.polygon(star_points, fill=star_color)

# Afficher le drapeau de la Turquie
image.show()
