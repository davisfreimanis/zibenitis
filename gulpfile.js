var gulp = require('gulp');
var gutil = require('gulp-util');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('log', function () {
    gutil.log('Test log');
});

gulp.task('sass', function () {
    gulp.src('static-loc/scss/style.scss')
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('static-loc'));
});

gulp.task('watch', function () {
    gulp.watch('static-loc/scss/base/*.scss', ['sass']);
});

gulp.task('default', ['sass', 'watch']);