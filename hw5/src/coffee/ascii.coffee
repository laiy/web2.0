#	> File Name: ascii.coffee
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Friday, December 12, 2014 AM10:18:14 CST

$ ->
    animation = false
    frameContainer = []
    interval = null
    frame = -1
    itv = 200

    $('#small').click ->
        $('#displayarea').css 'fontSize', '7pt'

    $('#medium').click ->
        $('#displayarea').css 'fontSize', '12pt'

    $('#large').click ->
        $('#displayarea').css 'fontSize', '24pt'

    $('#animation').change ->
        $('#displayarea').val ANIMATIONS[$('#animation').val()]
        animation = false
        frame = -1

    $('#start').click ->
        if not animation
            frameContainer = $('#displayarea').val().split '=====\n'
            interval = setInterval autoPlay, itv
            animation = true
            $('#stop').attr 'disabled', false
            $('#start').attr 'disabled', true
            $('#animation').attr 'disabled', true

    $('#stop').click ->
        if animation
            clearInterval interval
            animation = false
            frame = -1
            $('#displayarea').val ANIMATIONS[$('#animation').val()]
            $('#stop').attr 'disabled', true
            $('#start').attr 'disabled', false
            $('#animation').attr 'disabled', false

    $('#speed').click ->
        itv = if $('#speed').attr('checked') is 'checked' then 50 else 200
        if animation then clearInterval interval, interval = setInterval autoPlay, itv

    autoPlay = ->
        $('#displayarea').val frameContainer[++frame]
        frame = -1 if frame is frameContainer.length - 1

