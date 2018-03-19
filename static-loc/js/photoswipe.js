var openPhotoSwipe = function(startIndex) {
    var pswpElement = document.querySelectorAll('.pswp')[0];

    // define options (if needed)
    var options = {
        showAnimationDuration: 0,
        hideAnimationDuration: 0,
        index: startIndex
    };

    var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, window.djangoImages, options);
    gallery.init();
};