def on_right_pressed():
    mySprite2.x = mySprite2.x + 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

mySprite2: Sprite = None
mySprite3 = sprites.create(assets.image("""
    myImage
    """), SpriteKind.player)
mySprite = mySprite3
mySprite2 = sprites.create(assets.image("""
    myImage6
    """), SpriteKind.enemy)

def on_forever():
    music.play(music.string_playable("B A B G C5 A B F ", 120),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)

def on_forever2():
    global mySprite3
    pause(100)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    mySprite3 = sprites.create(assets.image("""
        myImage1
        """), SpriteKind.player)
    pause(100)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    mySprite3 = sprites.create(assets.image("""
        myImage0
        """), SpriteKind.player)
    pause(100)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    mySprite3 = sprites.create(assets.image("""
        myImage2
        """), SpriteKind.player)
    pause(100)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    mySprite3 = sprites.create(assets.image("""
        myImage0
        """), SpriteKind.player)
forever(on_forever2)
