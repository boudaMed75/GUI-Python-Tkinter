from PIL import Image, ImageDraw

# Dimensions du drapeau
width = 1200
height = 800






# Dessiner l'étoile
star_color = (255, 255, 255)
star_x = width // 2
star_y = height // 2
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
