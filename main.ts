controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite2.x = mySprite2.x + 1
})
let mySprite2: Sprite = null
let mySprite3 = sprites.create(assets.image`myImage`, SpriteKind.Player)
let mySprite = mySprite3
mySprite2 = sprites.create(assets.image`myImage6`, SpriteKind.Enemy)
forever(function () {
    music.play(music.stringPlayable("B A B G C5 A B F ", 120), music.PlaybackMode.UntilDone)
})
forever(function () {
    pause(100)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    mySprite3 = sprites.create(assets.image`myImage1`, SpriteKind.Player)
    pause(100)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    mySprite3 = sprites.create(assets.image`myImage0`, SpriteKind.Player)
    pause(100)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    mySprite3 = sprites.create(assets.image`myImage2`, SpriteKind.Player)
    pause(100)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    mySprite3 = sprites.create(assets.image`myImage0`, SpriteKind.Player)
})
