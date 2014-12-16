#	> File Name: pimpmytext.coffee
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Tuesday, December 16, 2014 PM03:15:52 CST

$ ->
    $('#bigger-pimpin').click ->
        setInterval ->
            $('textarea').css 'fontSize', parseInt($('textarea').css('fontSize')) + 2 + 'pt'
        , 500

    $('#bling').click ->
        $('textarea').css 'text-decoration', if $('#bling').attr('checked') is 'checked' then 'underline' else 'none'
        $('textarea').css 'font-weight', if $('#bling').attr('checked') is 'checked' then 'bold' else 'normal'
        $('textarea').css 'color', if $('#bling').attr('checked') is 'checked' then 'green' else 'black'
        $('textarea').css 'fontSize', if $('#bling').attr('checked') is 'checked' then '24pt' else '12pt'
        $('textarea').css 'padding', if $('#bling').attr('checked') is 'checked' then '10px' else '0'
        $('body').css 'background-image', if $('#bling').attr('checked') is 'checked' then 'url(hundred-dollar-bill.jpg)' else 'none'

    $('#snoopify').click ->
        $('textarea').val $('textarea').val().toUpperCase().split('\n').join '-izzle.\n'

