"""Simple placeholder model for the proposal template demo.

Not a real production design — just enough geometry (base, side rails,
roller, sensor housing) to prove the embedded 3D viewer works. Swap
sample.glb for your own export to use this template on a real job.
"""
from build123d import *

BASE_LENGTH, BASE_WIDTH, BASE_HEIGHT = 600, 300, 20
RAIL_HEIGHT, RAIL_THICKNESS = 60, 8
ROLLER_DIAMETER, ROLLER_LENGTH = 50, BASE_WIDTH - 2 * RAIL_THICKNESS
SENSOR_SIZE = 40

with BuildPart() as base:
    Box(BASE_LENGTH, BASE_WIDTH, BASE_HEIGHT)

with BuildPart() as rail_1:
    Box(BASE_LENGTH, RAIL_THICKNESS, RAIL_HEIGHT)
    rail_1 = rail_1.part.moved(Location((0, (BASE_WIDTH - RAIL_THICKNESS) / 2, (BASE_HEIGHT + RAIL_HEIGHT) / 2)))

with BuildPart() as rail_2:
    Box(BASE_LENGTH, RAIL_THICKNESS, RAIL_HEIGHT)
    rail_2 = rail_2.part.moved(Location((0, -(BASE_WIDTH - RAIL_THICKNESS) / 2, (BASE_HEIGHT + RAIL_HEIGHT) / 2)))

with BuildPart() as roller:
    with BuildSketch(Plane.YZ):
        Circle(radius=ROLLER_DIAMETER / 2)
    extrude(amount=ROLLER_LENGTH, both=True)
    roller = roller.part.moved(Location((0, 0, BASE_HEIGHT + ROLLER_DIAMETER / 2)))

with BuildPart() as sensor:
    Box(SENSOR_SIZE, SENSOR_SIZE, SENSOR_SIZE * 2)
    sensor = sensor.part.moved(Location((BASE_LENGTH / 2 - SENSOR_SIZE, 0, BASE_HEIGHT + RAIL_HEIGHT + SENSOR_SIZE)))

base.part.color = Color("DarkSlateGray")
rail_1.color = Color("DarkSlateGray")
rail_2.color = Color("DarkSlateGray")
roller.color = Color("Silver")
sensor.color = Color("Orange")

assembly = Compound(children=[base.part, rail_1, rail_2, roller, sensor])

if __name__ == "__main__":
    export_gltf(assembly, "sample.glb", binary=True)
    print("Saved sample.glb")
