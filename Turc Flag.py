from PIL import Image, ImageDraw

# Dimensions du drapeau
width = 1200
height = 800

# Créer une image rouge
image = Image.new('RGB', (width, height), 'red')
draw = ImageDraw.Draw(image)

# Dimensions et proportions de la lune et de l'étoile
moon_diameter = 400
star_radius = 120

# Dessiner la lune blanche
moon_color = (255, 255, 255)
moon_position = (width // 2 - moon_diameter // 2, height // 2 - moon_diameter // 2)
draw.ellipse((moon_position[0], moon_position[1], moon_position[0] + moon_diameter, moon_position[1] + moon_diameter), fill=moon_color)

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
