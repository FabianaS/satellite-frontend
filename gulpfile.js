var gulp = require('gulp');
var gulpBrowser = require("gulp-browser");
var reactify = require('reactify');
var del = require('del');
var size = require('gulp-size');


// tasks

gulp.task('transform', function () {
  var stream = gulp.src('./satellite/static/js/jsx/*.js')
    .pipe(gulpBrowser.browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./satellite/static/js'))
    .pipe(size());
  return stream;
});

gulp.task('del', function () {
  return del(['./satellite/static/scripts/js']);
});



gulp.task('default', function () {
  gulp.start('transform');
  gulp.watch('./satellite/static/js/jsx/*.js', ['transform']);
});