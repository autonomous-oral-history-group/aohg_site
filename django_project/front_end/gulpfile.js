'use strict';
 
var gulp = require('gulp');
var sass = require('gulp-sass');
var rename = require('gulp-rename');
var browserify = require('browserify');

//var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');
var log = require('gulplog');

var tap = require('gulp-tap');

 
sass.compiler = require('node-sass');
 
gulp.task('sass', function () {
  return gulp.src('./scss/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./css/'))
	 ;
});
 
gulp.task('watch', function () {
  gulp.watch('./src/styles/**/*.scss', ['sass']);
});


//https://github.com/gulpjs/gulp/blob/master/docs/recipes/browserify-with-globs.md
gulp.task('js', function () {
	return gulp.src('app/**/*.js', {read: false})
    // transform file objects using gulp-tap plugin
    .pipe(tap(function (file) {

      log.info('bundling ' + file.path);

      // replace file contents with browserify's bundle stream
      file.contents = browserify(file.path, {debug: true}).bundle();
    }))



    // transform streaming contents into buffer contents (because gulp-sourcemaps does not support streaming contents)
    .pipe(buffer())

    // load and init sourcemaps
    .pipe(sourcemaps.init({loadMaps: true}))

    .pipe(uglify())

    // write sourcemaps
    .pipe(sourcemaps.write('./'))

    .pipe(gulp.dest('js'));

	 
});
