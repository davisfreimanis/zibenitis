var gulp = require('gulp');
var gutil = require('gulp-util');
var livereload = require('gulp-livereload');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('html', function () {
    gulp.src('templates/**/*.html')
        .pipe(livereload());
});

gulp.task('sass', function () {
    gulp.src('static-loc/scss/style.scss')
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('static-loc'))
        .pipe(livereload());
});

gulp.task('watch', function () {
    livereload.listen();
    gulp.watch('static-loc/scss/base/*.scss', ['sass']);
    gulp.watch('templates/**/*.html', ['html']);
});

gulp.task('default', ['sass', 'html', 'watch']);