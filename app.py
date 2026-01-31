from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# 1. Initialize the Engine
app = Ursina()

# 2. Define Assets (You can change these strings to your file names later)
# If you have 'grass.png' in your folder, use texture='grass'
textures = {
    'grass': 'grass_block', # Placeholder for built-in texture
    'dirt':  'dirt_block',
    'stone': 'stone_block',
    'brick': 'brick'
}

current_texture = textures['grass']

# 3. Define the Block (Voxel) Logic
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture=textures['grass']):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            highlight_color=color.light_gray,
        )

    def input(self, key):
        if self.hovered:
            # Place Block
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture=current_texture)
            
            # Break Block
            if key == 'left mouse down':
                destroy(self)

# 4. Handle Keyboard Inputs for Block Selection
def update():
    global current_texture
    if held_keys['1']: current_texture = textures['grass']
    if held_keys['2']: current_texture = textures['dirt']
    if held_keys['3']: current_texture = textures['stone']
    if held_keys['4']: current_texture = textures['brick']

# 5. World Generation (A simple 15x15 floor)
for z in range(15):
    for x in range(15):
        Voxel(position=(x, 0, z))

# 6. Player and Environment
player = FirstPersonController()
sky = Sky() # Adds a simple background sky

# 7. Run the App
app.run()
