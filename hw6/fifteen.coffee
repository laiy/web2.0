#	> File Name: fifteen.coffee
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Thursday, December 18, 2014 AM09:45:50 CST

class Piece
    constructor: (@col, @row, @id, @element)->

class Maze
    constructor: (@pieces = [], @blankPosition = 16)->

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
                @push piece
                row++
            col++

    initializePieceElement: ->
        for piece in @pieces
            if piece.element isnt undefined
                piece.element.style.backgroundPosition = -(piece.row - 1) * 96 + "px " + -(piece.col - 1) * 96 + "px"
     
    updatePosition: ->
        blankCol = Math.ceil @blankPosition / 4
        blankRow = if @blankPosition % 4 then @blankPosition % 4 else 4
        for piece in @pieces
            if piece.element isnt undefined
                piece.element.style.left = (piece.row - 1) * 96 + "px"
                piece.element.style.top = (piece.col - 1) * 96 + "px"
                if Math.abs(piece.row - blankRow) + Math.abs(piece.col - blankCol) > 1
                    piece.element.className = 'puzzlepiece'
                else
                    piece.element.className = 'puzzlepiece movablepiece'

maze = new Maze

window.onload = ->
    maze.initialize()

