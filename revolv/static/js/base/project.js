$(document).ready(function () {
    draw();
});

$( window ).resize(function() {
    $(".project-badge-circle-grouping").remove();
    $(".project-badge-partial-grouping").remove();
    $(".project-badge-circle").remove();
    $(".project-badge-line" ).remove();
    $(".outside-circle" ).remove();
    draw();
});

/**
 * Dynamically resizes text inside the speedometer, resizes the iframe, draws an outside circle, and draws an inner
 * partial circle based on the width of the existing screen.
 */
var draw = function() {

    var radius = $(document).width() * 0.12;
    setTextSize(radius);
    resizeIframe();
    //Common drawCircle functionality has been moved util.js
    drawCircle(radius,1);
};
