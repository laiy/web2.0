#	> File Name: Gruntfile.coffee
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Sunday, November 23, 2014 AM10:42:51 CST

module.exports = (grunt)->
    grunt.initConfig
        watch:
            compile:
                files: [
                    'src/coffee/**/*.coffee'
                ]
                options:
                    spawn: false
                tasks: 'coffee'
        coffee:
            glob_to_multiple:
                expand: true,
                flatten: true,
                cwd: 'src/coffee',
                src: ['**/*.coffee']
                dest: 'bin/js',
                ext: '.js'

    grunt.loadNpmTasks 'grunt-contrib-coffee'
    grunt.loadNpmTasks 'grunt-contrib-watch'

    grunt.registerTask 'default', 'watch'
