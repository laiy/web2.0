#	> File Name: maze.coffee
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Thursday, December 18, 2014 AM09:12:15 CST

$ ->
    youLose = false

    lose = ->
        if not youLose
            $('.boundary').addClass 'youlose'
            $('#status').html('You lose!')
            youLose = true

    $('.boundary').mouseover ->
        lose()

    $('#maze').mouseleave ->
        lose()

    $('#start').click ->
        $('.boundary').removeClass 'youlose'
        youLose = false

    $('#end').mouseover ->
        if not youLose
            $('#status').html('You win!')
            youLose = true

