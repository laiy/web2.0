#	> File Name: fifteen.coffee
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Thursday, December 18, 2014 AM09:45:50 CST

class Piece
    constructor: (@col, @row, @id, @element)->

class Maze
    constructor: (@pieces = [], @blankCol = 4, @blankRow = 4)->

    push: (piece)->
        @pieces.push piece

    initialize: ->
        @initializeDataStructure()
        @initializePieceElement()
        @updatePosition()
        that = @
        document.getElementById('shufflebutton').addEventListener 'click', ->
            that.shuffle(that)

    initializeDataStructure: ->
        col = 1
        pieces = document.getElementById('puzzlearea').getElementsByTagName 'div'
        while col < 5
            row = 1
            while row < 5
                piece = new Piece col, row, (col - 1) * 4 + row, pieces[(col - 1) * 4 + row - 1]
                if piece.element isnt undefined
                    @push piece
                    onePiece = @pieces[(col - 1) * 4 + row - 1]
                    that = @
                    ele = onePiece.element
                    onePiece.element.onclick = do (ele)->
                        ->
                            that.pieceClickHandler(ele)
                row++
            col++

    initializePieceElement: ->
        for piece in @pieces
            if piece.element isnt undefined
                piece.element.style.backgroundPosition = -(piece.row - 1) * 96 + "px " + -(piece.col - 1) * 96 + "px"
     
    updatePosition: ->
        for piece in @pieces
            if piece.element isnt undefined
                piece.element.style.left = (piece.row - 1) * 96 + "px"
                piece.element.style.top = (piece.col - 1) * 96 + "px"
                if Math.abs(piece.row - @blankRow) + Math.abs(piece.col - @blankCol) > 1
                    piece.element.className = 'puzzlepiece'
                else
                    piece.element.className = 'puzzlepiece movablepiece'

    pieceClickHandler: (ele)->
        index = parseInt ele.textContent
        if Math.abs(@pieces[index - 1].row - @blankRow) + Math.abs(@pieces[index - 1].col - @blankCol) <= 1
            @move index
            @updatePosition()
            if @completed()
                alert 'You Win!'
                @shuffle()

    move: (index)->
        @pieces[index - 1].col ^= @blankCol
        @blankCol ^= @pieces[index - 1].col
        @pieces[index - 1].col ^= @blankCol
        @pieces[index - 1].row ^= @blankRow
        @blankRow ^= @pieces[index - 1].row
        @pieces[index - 1].row ^= @blankRow

    completed: ->
        index = 1
        while index <= 15
            if (@pieces[index - 1].col - 1) * 4 + @pieces[index - 1].row isnt @pieces[index - 1].id
                return false
            index++
        return true

    shuffle: (that)->
        times = 100
        while times > 0
            randomNumberX = Math.round Math.random()
            randomNumberY = Math.round Math.random()
            if that
                that.randomMove(randomNumberX, randomNumberY)
            else
                @randomMove(randomNumberX, randomNumberY)
            times--

    randomMove: (randomNumberX, randomNumberY)->
        col = @blankCol
        row = @blankRow
        if randomNumberX
            col = if randomNumberY and @isValid(col + 1) then col + 1 else if @isValid(col - 1) then col - 1 else col
        else
            row = if randomNumberY and @isValid(row + 1) then row + 1 else if @isValid(row - 1) then row - 1 else row
        if col isnt @blankCol or row isnt @blankRow
            if (col - 1) * 4 + row isnt 16
                @move (col - 1) * 4 + row
                @updatePosition()

    isValid: (position)->
        console.log 'position' + position
        return if position >= 1 and position <= 4 then true else false

maze = new Maze

window.onload = ->
    maze.initialize()

