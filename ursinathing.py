from ursina import *
import random

random_generator = random.Random()
app = Ursina()
cube_texture = load_texture('dirt_block.png')
window.title = 'ursina idk'
window.borderless = False  
window.exit_button.visible = False

Text.default_resolution = 1080 * Text.size
copyright = Text(origin=(3.3,19.1), background=False)
name = Text(origin=(-5.5,-19.1), background=False)

def input(key):
    if key == 'right mouse down':
        camera.position =(0,0,-20)
        cube.color=color.white

def update():
    cube.rotation_y += time.dt * 100
    cube.rotation_x += time.dt * 100
    if held_keys['w']:               
        camera.position += (0, time.dt * 2, 3)           
    if held_keys['s']:                              
        camera.position -= (0, time.dt * 2, 3) 
    if held_keys['a']:     
        camera.position -= (0.5, time.dt, 0)
    if held_keys['d']:
        camera.position += (0.5, time.dt, 0)
    if held_keys['up arrow']:
        camera.position += (0, time.dt * 50, 0)
    if held_keys['down arrow']:
        camera.position -= (0, time.dt * 50, 0)
    if held_keys['space']:
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        cube.color = color.rgb(red, green, blue)

cube = Entity(model='cube', color=color.white, scale=(2,2,2), texture = cube_texture, position =(0,0.3,0))
copyright.text = 'Made by extoplasm'
name.text = 'obama spin'
app.run()