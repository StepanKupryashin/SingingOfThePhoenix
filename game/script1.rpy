
# Метка splashscreen автоматически запсукается при старте игры перед главным меню.
label splashscreen:
    # Показываем чёрный экран
    scene black
    # Ждём полсекунды
    pause(0.5)
    # Проиграть указанное видео.
    $ renpy.movie_cutscene('videos/logo.webm')
    pause(1)

#все звуки в игре
define audio.new_scen = "audio/new_scen.mp3" #печатающая машинка
define audio.budilnik = "audio/budilnik_1.mp3" #будильник
define audio.costi = "audio/costi perelom.mp3" #звук удара
define audio.perelom = "audio/perelom.mp3" #звук удара
define audio.baraban = "audio/baraban.mp3" #
define audio.hlopok = "audio/hlopok dveri.mp3" #хлопок двери
define audio.Grustnaya_melodiya = "audio/Grustnaya_melodiya.mp3" # пианино с дождём
define audio.door_opening = "audio/door_opening.mp3" #
define audio.huum = "audio/huum.mp3" # звук людей
define audio.hum = "audio/hum.mp3" # розовый шум
define audio.zvonok = "audio/zvonok.mp3" # школьный звонок
define audio.knopka = "audio/knopka.ogg" # нажатие в меню
define audio.monetku = "audio/monetku.mp3" # падение монет
define audio.v_ruke = "audio/v_ruke.mp3" #
define audio.limonad = "audio/limonad.mp3" #
define audio.stuk_kablukov = "audio/stuk_kablukov.mp3" #
define audio.ptica = "audio/ptica.mp3" #
define audio.vshlip = "audio/vshlip.mp3" #
define audio.zvuk_mikrovolnovki = "audio/zvuk_mikrovolnovki.mp3" #
define audio.mikrovolnovka_off = "audio/mikrovolnovka_off.mp3" #
define audio.cyst_0 = "audio/cyst_0.mp3" #
define audio.cyst = "audio/cyst.mp3" #
define audio.contysia = "audio/contysia.mp3" #контузия
define audio.Son_Fon = "audio/Son_Fon.mp3" # Фон для сна 1
define audio.serdse = "audio/serdse.mp3" # сердцебиение спокойное
define audio.serdse_fast = "audio/serdse_fast.mp3" # сердцебиение частое
define audio.duxanie = "audio/duxanie.mp3" # дыхание спокойное
define audio.duxanie_fast = "audio/duxanie_fast.mp3" # дыхание ускоренное
define audio.shagi = "audio/shagi.mp3" # шаги с гулом
define audio.horror = "audio/horror.mp3" # скример
define audio.mexanizm = "audio/mexanizm.mp3" # тикание
define audio.capcan = "audio/capcan.mp3" # удар по железу

# Звуковой канал "music2 и music3", которые будут проигрываться по кругу
# Звуковой канал "sound2", который не будет проигрываться по кругу, громкость привязана к громкости остальных звуков
init python:
    renpy.music.register_channel("music2", loop=True, mixer="sfx")
    renpy.music.register_channel("music3", loop=True, mixer="sfx")
    renpy.music.register_channel("music4", loop=True, mixer="sfx")
    renpy.music.register_channel("music5", loop=True, mixer="sfx")
    renpy.music.register_channel("sound2", loop=False, mixer="sfx")
    renpy.music.register_channel("sound3", loop=False, mixer="sfx")


init python:
    # объявление картинок и псевдонимов
    images_auto()

    # функции громыхания для внедрения в картинки
    def s_thunder1(trans, st, at):
        splay("thunder1")

    def s_thunder2(trans, st, at):
        splay("thunder2")

    def s_thunder3(trans, st, at):
        splay("thunder3")

    def s_rain(trans, st, at):
        sfxplay("rain")

    # остановка шума дождя
    def s_rain_off(trans, st, at):
        sfxstop()

init:
    # анимация дождя
    image rain ani = Ani("rain ", 8, .1, zoom=2.4)

    # анимация молнии
    image light ani = Ani("lightning ", 3, .05, True, True)

    $ t1, t2, t3 = rndf(8, 15), rndf(12, 20), rndf(15, 25)
    $ t11, t22, t33 = rndf(2, 4), rndf(5, 7), rndf(7, 10)
    $ xz = (1, -1)
    # мерцание молнии
    transform l_flash(t, tt):
        anchor (.5, .0)
        xzoom xz[rnd(1)]
        alpha 0
        tt
        alpha 1
        .1
        alpha 0
        .1
        alpha 1
        .1
        alpha 0
        t - tt - .3
        repeat

    image light1 = At("light ani", l_flash(t1, t11))
    image light2 = At("light ani", l_flash(t2, t22))
    image light3 = At("light ani", l_flash(t3, t33))

    # картинка с молнией и со звуком грома
    image thunder:
        contains:
            "light1"
            align(rndf(.0, 1.), .0)
            t11
            function s_thunder1
            t1 - t11
            repeat
        contains:
            "light2"
            align(rndf(.0, 1.), .0)
            t22
            function s_thunder2
            t2 - t22
            repeat
        contains:
            "light3"
            align(rndf(.0, 1.), .0)
            t33
            function s_thunder3
            t3 - t33
            repeat

    # картинка с дождём и со звуком дождя
    image rain:
        "rain ani"
        on show:
            function s_rain
        on hide:
            function s_rain_off






#персонажи
define s = Character('Сильвия', kind=nvl, color="#c8ffc8")
define M = Character("Майко", color="#FF0000", image= "maiko")
define T = Character("Тадзай", color="#32CD32")
define U = Character("Юн-Юн", color="#8B008B", image= "un")
define n = Character(None, kind=nvl)
define Y = Character("Учитель", color="#F0E68C", image= "himmel")
#открытие глаз "with onn"
init python:
    onn = ImageDissolve("eye.png", 1.5, 20, reverse=False)
    onn_05 = ImageDissolve("exz.png", 0.05, 5, reverse=True)
    off = ImageDissolve("eye.png", 2.0, 20, reverse=True)
    off_fast = ImageDissolve("eye.png", 1.0, 20, reverse=True)


#уход вправа медленно
transform move_slide:
    linear 3.0 xalign 0.89

#уход вправа быстро
transform move_slide_fast:
    linear 1.00 xalign 1.99
