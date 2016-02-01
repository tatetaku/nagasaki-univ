#!/usr/bin/ python
import mcpi.minecraft as minecraft
import mcpi.block as block
import math

mc = minecraft.Minecraft.create("localhost")
pos = mc.player.getPos()

pos.x = -1061
pos.y = 4
pos.z = -99

pos.x += 1931
pos.y += -4
pos.z += 899

cnt = 0
cnt2 = 0

hankei = 32

for i in range(-18, 18):
    for j in range(0, 12):
        for k in range(-6, 6):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.SANDSTONE.id)


for i in range(-17, 17):
    for j in range(1, 11):
        for k in range(-5, 5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.AIR.id)

for i in range(-19, 19):
    for j in range(11, 12):
        for k in range(-7, 7):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.WOOL.id)

for i in range(-17, -13):
    for j in range(2, 5):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(-17, -13):
    for j in range(7, 10):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(-11, -7):
    for j in range(2, 5):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(-11, -7):
    for j in range(7, 10):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(-5, -1):
    for j in range(2, 5):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(-5, -1):
    for j in range(7, 10):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(1, 5):
    for j in range(2, 5):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(1, 5):
    for j in range(7, 10):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)


for i in range(7, 11):
    for j in range(2, 5):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(7, 11):
    for j in range(7, 10):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)


for i in range(13, 17):
    for j in range(2, 5):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)

for i in range(13, 17):
    for j in range(7, 10):
        for k in range(-6, -5):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.GLASS.id)


'''
for t in range(0, 36000):
    cnt = cnt + 1
    cnt2 = cnt2 + 1
    if cnt == 60:
        pos.y = pos.y + 1
        cnt = 0
        if cnt2 == 360:
            hankei = hankei - 1
            cnt2 = 0
    mc.setBlock(hankei * math.cos(math.radians(t)) + pos.x, pos.y,  hankei *  math.sin(math.radians(t)) + pos.z, block.BRICK_BLOCK.id)
    mc.setBlock(hankei * math.cos(math.radians(t)) + pos.x, pos.y+1,  hankei *  math.sin(math.radians(t)) + pos.z, block.GRASS.id)
    mc.setBlock((hankei-1) * math.cos(math.radians(t)) + pos.x, pos.y,  (hankei-1) *  math.sin(math.radians(t)) + pos.z, block.BRICK_BLOCK.id)
    mc.setBlock((hankei-2) * math.cos(math.radians(t)) + pos.x, pos.y,  (hankei-2) *  math.sin(math.radians(t)) + pos.z, block.BRICK_BLOCK.id)
    if (hankei - 2) == 0:
        break
'''
