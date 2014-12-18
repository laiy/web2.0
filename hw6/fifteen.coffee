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

    initializeDataStructure: ->
        col = 1
        pieces = document.getElementById('puzzlearea').getElementsByTagName 'div'
        while col < 5
            row = 1
            while row < 5
                piece = new Piece col, row, (col - 1) * 4 + row, pieces[(col - 1) * 4 + row - 1]
                if piece.element isnt undefined
                    piece.element.onclick = @pieceClickHandler
                @push piece
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

    pieceClickHandler: ->
        index = parseInt @.textContent
        if Math.abs(maze.pieces[index - 1].row - @blankRow) + Math.abs(@pieces[index - 1].col - @blankCol) <= 1
            @move(index)
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
            if (@pieces[index - 1].col - 1) * 4 + row isnt @pieces[index - 1].id
                return false
            index++
        return true

    shuffle: ->
        alert 'shuffle'

maze = new Maze

window.onload = ->
    maze.initialize()

